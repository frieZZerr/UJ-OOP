package com.example.project_9

import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

class ProductDetailActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_product_detail)

        val productName = intent.getStringExtra("productName") ?: ""
        val productPrice = intent.getDoubleExtra("productPrice", 0.0)
        val productDescription = intent.getStringExtra("productDescription") ?: ""

        findViewById<TextView>(R.id.detailProductName).text = productName
        findViewById<TextView>(R.id.detailProductPrice).text = "${productPrice} zł"
        findViewById<TextView>(R.id.detailProductDescription).text = productDescription

        findViewById<android.widget.Button>(R.id.backButton).setOnClickListener {
            finish()
        }

        findViewById<android.widget.Button>(R.id.addToCartButton).setOnClickListener {
            android.widget.Toast.makeText(this, "Added to Cart: $productName", android.widget.Toast.LENGTH_SHORT).show()
        }
    }
}
