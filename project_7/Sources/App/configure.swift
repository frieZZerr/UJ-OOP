import Fluent
import FluentSQLiteDriver
import Vapor
import Leaf

public func configure(_ app: Application) throws {
    app.middleware.use(FileMiddleware(publicDirectory: app.directory.publicDirectory))
    app.middleware.use(app.sessions.middleware)

    app.views.use(.leaf)

    app.databases.use(.sqlite(.file("db.sqlite")), as: .sqlite)

    app.migrations.add(CreateProduct())

    try app.autoMigrate().wait()

    try routes(app)
}
