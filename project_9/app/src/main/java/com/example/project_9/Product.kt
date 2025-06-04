package com.example.project_9

data class Product(
    val id: Int,
    val name: String,
    val price: Double,
    val categoryId: Int,
    val description: String,
    val imageUrl: String = ""
)
