package com.example.project_9

import android.os.Bundle
import android.widget.TextView
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class ProductDetailActivity : AppCompatActivity() {

    private lateinit var addToCartButton: Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_product_detail)

        val productId = intent.getIntExtra("productId", -1)
        val productName = intent.getStringExtra("productName") ?: ""
        val productPrice = intent.getDoubleExtra("productPrice", 0.0)
        val productDescription = intent.getStringExtra("productDescription") ?: ""
        val categoryId = intent.getIntExtra("categoryId", 1)

        findViewById<TextView>(R.id.detailProductName).text = productName
        findViewById<TextView>(R.id.detailProductPrice).text = "${productPrice} zł"
        findViewById<TextView>(R.id.detailProductDescription).text = productDescription

        addToCartButton = findViewById(R.id.addToCartButton)

        findViewById<Button>(R.id.backButton).setOnClickListener {
            finish()
        }

        addToCartButton.setOnClickListener {
            val product = Product(productId, productName, productPrice, categoryId, productDescription)

            CartManager.addToCart(product)
            Toast.makeText(this, "Added to cart: $productName", Toast.LENGTH_SHORT).show()

            updateButtonText()
        }

        updateButtonText()
    }

    private fun updateButtonText() {
        val productId = intent.getIntExtra("productId", -1)
        val isInCart = CartManager.isProductInCart(productId)

        if (isInCart) {
            val cartItem = CartManager.cartItems.find { it.product.id == productId }
            addToCartButton.text = "In cart (${cartItem?.quantity ?: 0})"
        } else {
            addToCartButton.text = "Add to cart"
        }
    }
}
