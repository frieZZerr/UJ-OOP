package com.example.project_9

import android.content.Intent
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class ProductListActivity : AppCompatActivity() {

    private lateinit var productsRecyclerView: RecyclerView
    private lateinit var productAdapter: ProductAdapter
    private lateinit var titleTextView: TextView
    private val products = mutableListOf<Product>()
    private var categoryId: Int = 0

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_product_list)

        categoryId = intent.getIntExtra("categoryId", 0)
        val categoryName = intent.getStringExtra("categoryName") ?: ""

        setupViews(categoryName)
        loadProducts()
    }

    private fun setupViews(categoryName: String) {
        titleTextView = findViewById(R.id.titleTextView)
        productsRecyclerView = findViewById(R.id.productsRecyclerView)

        titleTextView.text = categoryName
        productsRecyclerView.layoutManager = LinearLayoutManager(this)

        productAdapter = ProductAdapter(products) { product ->
            showProductDetails(product)
        }
        productsRecyclerView.adapter = productAdapter
    }

    private fun loadProducts() {
        when (categoryId) {
            1 -> { // Electronics
                products.apply {
                    add(Product(1, "Smartphone Samsung", 2999.99, 1, "Newest model with 108MP camera", "https://img.gkbcdn.com/p/2019-10-25/samsung-galaxy-s10-4g-6-1-inch-8gb-128gb-smartphone-black-1574132936482._w500_p1_.jpg"))
                    add(Product(2, "Laptop Dell", 3499.99, 1, "Laptop for work and entertainment"))
                    add(Product(3, "Earbuds Sony", 299.99, 1, "Wireless earbuds with ANC"))
                }
            }
            2 -> { // Clothes
                products.apply {
                    add(Product(4, "T-shirt Adidas", 89.99, 2, "100% cotton made sport t-shirt"))
                    add(Product(5, "Jeans Levi's", 249.99, 2, "Classic slim fit jeans"))
                    add(Product(6, "Sneakers Nike", 399.99, 2, "Sport shoes for running"))
                }
            }
            3 -> { // Books
                products.apply {
                    add(Product(7, "The Witcher - Blood of the Elves - Andrzej Sapkowski", 39.99, 3, "First part of 'The Witcher' saga"))
                    add(Product(8, "Clean Code", 79.99, 3, "Programming tutorials"))
                    add(Product(9, "Kotlin in Action", 89.99, 3, "Kotlin tutorial"))
                }
            }
            4 -> { // House & Garden
                products.apply {
                    add(Product(10, "Vacuum cleaner Dyson", 1299.99, 4, "Wireless vacuum cleaner"))
                    add(Product(11, "Potted plant", 29.99, 4, "Monstera deliciosa"))
                    add(Product(12, "Tool kit", 149.99, 4, "Complete DIY kit"))
                }
            }
            5 -> { // Sport
                products.apply {
                    add(Product(13, "Football Adidas", 79.99, 5, "Official football"))
                    add(Product(14, "Yoga mat", 49.99, 5, "Anti-slip fitness mat"))
                    add(Product(15, "Dumbbells 2x5kg", 99.99, 5, "Cast iron dumbbells for exercise"))
                }
            }
        }
        productAdapter.notifyDataSetChanged()
    }

    private fun showProductDetails(product: Product) {
        try {
            val intent = Intent(this, ProductDetailActivity::class.java)
            intent.putExtra("productId", product.id)
            intent.putExtra("productName", product.name)
            intent.putExtra("productPrice", product.price)
            intent.putExtra("productDescription", product.description)
            startActivity(intent)
        } catch (e: Exception) {
            android.widget.Toast.makeText(
                this,
                "Error: ${e.message}",
                android.widget.Toast.LENGTH_LONG
            ).show()
        }
    }
}
