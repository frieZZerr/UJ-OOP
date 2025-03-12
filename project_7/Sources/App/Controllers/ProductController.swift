import Vapor
import Fluent

struct ProductController: RouteCollection {
    func boot(routes: RoutesBuilder) throws {
        let products = routes.grouped("products")

        products.get(use: index)
        products.get("create", use: create)
        products.post(use: store)
        products.get(":id", use: show)
        products.get(":id", "edit", use: edit)
        products.post(":id", use: update)
        products.post(":id", "delete", use: delete)
    }

    // GET /products
    func index(req: Request) async throws -> View {
        let products = try await Product.query(on: req.db).all()
        return try await req.view.render("products/index", ["products": products])
    }

    // GET /products/create
    func create(req: Request) async throws -> View {
        return try await req.view.render("products/create")
    }

    // POST /products
    func store(req: Request) async throws -> Response {
        let input = try req.content.decode(ProductInput.self)

        let product = Product(
            name: input.name,
            price: input.price,
            description: input.description,
            isAvailable: input.isAvailable
        )

        try await product.save(on: req.db)

        return req.redirect(to: "/products")
    }

    // GET /products/:id
    func show(req: Request) async throws -> View {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }

        return try await req.view.render("products/show", ["product": product])
    }

    // GET /products/:id/edit
    func edit(req: Request) async throws -> View {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }

        return try await req.view.render("products/edit", ["product": product])
    }

    // POST /products/:id
    func update(req: Request) async throws -> Response {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }

        let input = try req.content.decode(ProductInput.self)

        product.name = input.name
        product.price = input.price
        product.description = input.description
        product.isAvailable = input.isAvailable

        try await product.save(on: req.db)

        return req.redirect(to: "/products")
    }

    // POST /products/:id/delete
    func delete(req: Request) async throws -> Response {
        guard let product = try await Product.find(req.parameters.get("id"), on: req.db) else {
            throw Abort(.notFound)
        }

        try await product.delete(on: req.db)

        return req.redirect(to: "/products")
    }
}
