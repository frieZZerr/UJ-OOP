package com.example.project_9

import android.content.Intent
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import android.widget.TextView

class MainActivity : AppCompatActivity() {

    private lateinit var categoriesRecyclerView: RecyclerView
    private lateinit var categoryAdapter: CategoryAdapter
    private val categories = mutableListOf<Category>()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        setupViews()
        loadCategories()
    }

    private fun setupViews() {
        categoriesRecyclerView = findViewById(R.id.categoriesRecyclerView)
        categoriesRecyclerView.layoutManager = LinearLayoutManager(this)

        categoryAdapter = CategoryAdapter(categories) { category ->
            openProductList(category)
        }
        categoriesRecyclerView.adapter = categoryAdapter
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
}
