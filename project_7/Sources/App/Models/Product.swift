import Fluent
import Vapor

final class Product: Model, Content, @unchecked Sendable {
    static let schema = "products"

    @ID(key: .id)
    var id: UUID?

    @Field(key: "name")
    var name: String

    @Field(key: "price")
    var price: Double

    @Field(key: "description")
    var description: String

    @Field(key: "is_available")
    var isAvailable: Bool

    init() {}

    init(id: UUID? = nil, name: String, price: Double, description: String, isAvailable: Bool) {
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.isAvailable = isAvailable
    }
}
