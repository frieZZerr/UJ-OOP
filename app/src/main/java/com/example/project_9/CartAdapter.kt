package com.example.project_9

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class CartAdapter(
    private val cartItems: MutableList<CartItem>,
    private val onItemChanged: () -> Unit
) : RecyclerView.Adapter<CartAdapter.CartViewHolder>() {

    class CartViewHolder(view: View) : RecyclerView.ViewHolder(view) {
        val productName: TextView = view.findViewById(R.id.cartProductName)
        val productPrice: TextView = view.findViewById(R.id.cartProductPrice)
        val quantityText: TextView = view.findViewById(R.id.quantityText)
        val decreaseButton: Button = view.findViewById(R.id.decreaseButton)
        val increaseButton: Button = view.findViewById(R.id.increaseButton)
        val removeButton: Button = view.findViewById(R.id.removeButton)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CartViewHolder {
        val view = LayoutInflater.from(parent.context)
            .inflate(R.layout.item_cart, parent, false)
        return CartViewHolder(view)
    }

    override fun onBindViewHolder(holder: CartViewHolder, position: Int) {
        val cartItem = cartItems[position]
        
        holder.productName.text = cartItem.product.name
        holder.productPrice.text = "${String.format("%.2f", cartItem.product.price)} zł"
        holder.quantityText.text = cartItem.quantity.toString()

        holder.decreaseButton.setOnClickListener {
            if (cartItem.quantity > 1) {
                cartItem.quantity--
                holder.quantityText.text = cartItem.quantity.toString()
                onItemChanged()
            }
        }

        holder.increaseButton.setOnClickListener {
            cartItem.quantity++
            holder.quantityText.text = cartItem.quantity.toString()
            onItemChanged()
        }

        holder.removeButton.setOnClickListener {
            cartItems.removeAt(position)
            notifyItemRemoved(position)
            notifyItemRangeChanged(position, cartItems.size)
            onItemChanged()
        }
    }

    override fun getItemCount() = cartItems.size
}
