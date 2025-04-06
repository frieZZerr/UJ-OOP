package com.example.demo.service

import org.springframework.stereotype.Service

@Service
class AuthService {

    private val users = mapOf(
        "alice" to "password123",
        "bob" to "qwerty",
        "charlie" to "letmein"
    )

    fun authenticate(username: String, password: String): Boolean {
        return users[username] == password
    }
}
