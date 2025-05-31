package com.example.project_9

import android.content.Intent
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class MainActivity : AppCompatActivity() {

    private lateinit var categoriesRecyclerView: RecyclerView
    private lateinit var categoryAdapter: CategoryAdapter
    private lateinit var cartButton: Button
    private lateinit var cartCountText: TextView
    private val categories = mutableListOf<Category>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        setupViews()
        loadCategories()
        updateCartCount()
    }

    override fun onResume() {
        super.onResume()
        updateCartCount()
    }

    private fun setupViews() {
        categoriesRecyclerView = findViewById(R.id.categoriesRecyclerView)
        cartButton = findViewById(R.id.cartButton)
        cartCountText = findViewById(R.id.cartCountText)

        categoriesRecyclerView.layoutManager = LinearLayoutManager(this)

        categoryAdapter = CategoryAdapter(categories) { category ->
            openProductList(category)
        }
        categoriesRecyclerView.adapter = categoryAdapter

        cartButton.setOnClickListener {
            val intent = Intent(this, CartActivity::class.java)
            startActivity(intent)
        }
    }

    private fun loadCategories() {
        categories.apply {
            add(Category(1, "Electronics", "📱"))
            add(Category(2, "Clothes", "👕"))
            add(Category(3, "Books", "📚"))
            add(Category(4, "House & Garden", "🏠"))
            add(Category(5, "Sport", "⚽"))
        }
        categoryAdapter.notifyDataSetChanged()
    }

    private fun openProductList(category: Category) {
        val intent = Intent(this, ProductListActivity::class.java)
        intent.putExtra("categoryId", category.id)
        intent.putExtra("categoryName", category.name)
        startActivity(intent)
    }

    private fun updateCartCount() {
        val count = CartManager.getItemCount()
        cartCountText.text = count.toString()
        cartCountText.visibility = if (count > 0) View.VISIBLE else View.GONE
    }
}
