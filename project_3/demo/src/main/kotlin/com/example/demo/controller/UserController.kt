package com.example.demo.controller

import com.example.demo.model.LoginRequest
import com.example.demo.model.User
import com.example.demo.service.AuthService
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.web.bind.annotation.*

@RestController
@RequestMapping("/users")
class UserController {

    @Autowired
    private lateinit var authService: AuthService

    private val allUsers = listOf(
        User(1, "alice"),
        User(2, "bob"),
        User(3, "charlie")
    )

    @GetMapping
    fun getAllUsers(): List<User> = allUsers

    @PostMapping("/login")
    fun login(@RequestBody loginRequest: LoginRequest): String {
        return if (authService.authenticate(loginRequest.username, loginRequest.password)) {
            "Login successful"
        } else {
            "Login failed"
        }
    }
}
