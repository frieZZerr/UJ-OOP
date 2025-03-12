package com.example.demo.controller

import com.example.demo.model.User
import org.springframework.web.bind.annotation.GetMapping
import org.springframework.web.bind.annotation.RequestMapping
import org.springframework.web.bind.annotation.RestController

@RestController
@RequestMapping("/users")
class UserController {

    private val users = listOf(
        User(1, "alice"),
        User(2, "bob"),
        User(3, "charlie")
    )

    @GetMapping
    fun getAllUsers(): List<User> = users
}
