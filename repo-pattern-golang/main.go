package main

import (
	"fmt"

	"github.com/nikhilakki/nikhilakki.in-blog-code-examples/repo-pattern-golang/models"
	"github.com/nikhilakki/nikhilakki.in-blog-code-examples/repo-pattern-golang/repositories"
)

func main() {
	userRepo := repositories.NewMockUserRepository()

	// Try to fetch a user by ID
	user, err := repositories.GetUserByID(userRepo, 1)
	if err != nil {
		fmt.Println("Error:", err)
	} else {
		fmt.Printf("User found: %+v\n", *user)
	}

	// Try to create a new user
	newUser, err := userRepo.Create(models.User{ID: 4, Name: "Nikhil Akki", Email: "me@nikhilakki.in"})
	if err != nil {
		fmt.Println("Error creating user:", err)
	} else {
		fmt.Printf("New user added: %+v\n", *newUser)
	}
}
