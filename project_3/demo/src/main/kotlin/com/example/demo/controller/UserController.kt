package com.example.demo.controller

import com.example.demo.model.User
import com.example.demo.service.AuthService
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/users")
class UserController(
    private val authService: AuthService
) {

    private val allUsers = listOf(
        User(1, "alice"),
        User(2, "bob"),
        User(3, "charlie")
    )

    @GetMapping
    fun getAllUsers(): List<User> = allUsers

    @PostMapping("/login")
    fun login(@RequestParam username: String, @RequestParam password: String): String {
        return if (authService.authenticate(username, password)) {
            "Login successful"
        } else {
            "Login failed"
        }
    }
}
