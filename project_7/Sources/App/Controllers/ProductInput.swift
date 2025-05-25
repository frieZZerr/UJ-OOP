import Vapor

struct ProductInput: Content {
    let name: String
    let price: Double
    let description: String
    let isAvailable: Bool
}
