package repositories

import (
	"errors"

	"github.com/nikhilakki/nikhilakki.in-blog-code-examples/repo-pattern-golang/models"
)

// UserRepository interface outlines methods to access user data.
type UserRepository interface {
	GetByID(id int) (*models.User, error)
	Create(user models.User) (*models.User, error)
}

// MockUserRepository simulates a repository handling data in memory.
type MockUserRepository struct {
	users []models.User // Pretend this slice is our database
}

// NewMockUserRepository initializes a new instance of MockUserRepository with some dummy data.
func NewMockUserRepository() *MockUserRepository {
	users := []models.User{
		{ID: 1, Name: "Arun Kutty", Email: "arun@example.com"},
		{ID: 2, Name: "Tarun Pai", Email: "tpai@example.com"},
	}
	return &MockUserRepository{users: users}
}

// GetByID looks for a user by ID and returns the user if found.
func (repo *MockUserRepository) GetByID(id int) (*models.User, error) {
	for _, user := range repo.users {
		if user.ID == id {
			return &user, nil
		}
	}
	return nil, errors.New("user not found")
}

// Create adds a new user to the repository.
func (repo *MockUserRepository) Create(user models.User) (*models.User, error) {
	repo.users = append(repo.users, user)
	return &user, nil
}

// In a real application, this function would be a part of the business logic layer
// that interacts with the repository layer.
func GetUserByID(repo UserRepository, id int) (*models.User, error) {
	return repo.GetByID(id)
}
