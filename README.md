# Object-oriented Programming

This is a repository for UJ Object-Oriented Programming. It will contain all the required projects. Each project will have it's own seperate branch with commit history.

The `master` branch will be constantly updated after each project has been finished.

## Project 1 - Paradigms (Pascal)

Write a Pascal program that contains two procedures. One generates a list of 50 random numbers from 0 to 100. The second procedure sorts the numbers using bubble sort.

:white_check_mark: 3.0 - [Procedure for generating 50 random numbers from 0 to 100](https://github.com/frieZZerr/UJ-OOP/commit/01af0d315f8387332cccf4077562b14c57e1f1ef)

:white_check_mark: 3.5 - [Procedure for sorting numbers](https://github.com/frieZZerr/UJ-OOP/commit/5e3ef3632f4afc73285d3923e054ffedd5216599)

:white_check_mark: 4.0 - [Adding parameters to the random procedure that specify the range: from, to, how many](https://github.com/frieZZerr/UJ-OOP/commit/a6d855aae07a421aa03121e0c8d2a1b8aaf502d0)

:white_check_mark: 4.5 - [5 unit tests testing the procedures](https://github.com/frieZZerr/UJ-OOP/commit/f6c8e33df635d695e841d21f10fd5c75bca51c24)

:white_check_mark: 5.0 - [Bash script to run the Pascal application via docker](https://github.com/frieZZerr/UJ-OOP/commit/377a2af19cc1fbdf746e1d9d89a5d1d22a26c569)

Code: [project_1](https://github.com/frieZZerr/UJ-OOP/tree/project_1)

## Project 2 - Architectural Patterns (Symfony + PHP)

Create a web application based on the Symfony framework. Any database can be used; SQLite is suggested.

:white_check_mark: 3.0 - [Create one model with a controller for products, following CRUD operations](https://github.com/frieZZerr/UJ-OOP/commit/6cfe1354bfda563bd58c4589d4487acf38c8e572)

:white_check_mark: 3.5 - [Create scripts to test endpoints via curl](https://github.com/frieZZerr/UJ-OOP/commit/a5a2fac3b25e90c8993798696368e260132d9d66)

:white_check_mark: 4.0 - [Create two additional controllers with their respective models](https://github.com/frieZZerr/UJ-OOP/commit/24d95caf9ee40ed8b88477ed7549a07a8ebaefdc)

:x: 4.5 - [Create views for all controllers]()

:x: 5.0 - [Create an administrative panel with mocked login functionality]()

Code: [project_2](https://github.com/frieZZerr/UJ-OOP/tree/project_2)

## Project 3 - Creational Patterns (Spring Boot + Kotlin)

Create a simple authorization service that simulates user authorization using a provided username and password. The service should be injected into the controller using the @Autowired annotation. The application should include a controller and be written in Kotlin. It should be based on the Spring Boot framework. The authorization service should be a singleton.

:white_check_mark: 3.0 - [Create a controller with data displayed from a list at an endpoint in JSON format](https://github.com/frieZZerr/UJ-OOP/commit/09bb34297f8f7b213bfb4ca1579ea1c5bfd498e8)

:white_check_mark: 3.5 - [Create an authorization class (mock) as a Singleton in eager form](https://github.com/frieZZerr/UJ-OOP/commit/f77745d93106aa265638f6d516fd42b26f88631a)

:white_check_mark: 4.0 - [Handle authorization data provided by the user](https://github.com/frieZZerr/UJ-OOP/commit/0b880c1e1953aa2ae8076e60ad7359c46fdc78f0)

:white_check_mark: 4.5 - [Inject the singleton into the main class via @Autowired](https://github.com/frieZZerr/UJ-OOP/commit/cc83d5f598517392b299a876b97cdb01432ada3c)

:white_check_mark: 5.0 - [Alongside the Eager version, provide a Singleton version in lazy form for selection](https://github.com/frieZZerr/UJ-OOP/commit/e543edc5b484039c39558b62b76c88534bcbdc34)

Code: [project_3](https://github.com/frieZZerr/UJ-OOP/tree/project_3)

## Project 4 - Structural Patterns (Echo + Go)

Create a Go application using the Echo framework. The application should have one endpoint and at least one proxy function that fetches stock market data from an external API. Requests to the endpoint can be sent as GET or POST.

:white_check_mark: 3.0 - [Create an application using the Echo framework in Go that will have a Stock controller, allowing the retrieval of stock market data](https://github.com/frieZZerr/UJ-OOP/commit/75097584d5824fee64b4d3eea70b0ad8d15c41e2)

:white_check_mark: 3.5 - [Create a Stock Market model using GORM, and load data from a list upon startup](https://github.com/frieZZerr/UJ-OOP/commit/db1de5a2eaa192f0c18820d58e1434b77ded219c)

:white_check_mark: 4.0 - [Create a proxy class that will fetch data from an external service during a request to our controller](https://github.com/frieZZerr/UJ-OOP/commit/9fecb51e316bde2d1c67fc3fef1d25bdaf8cdbb0)

:white_check_mark: 4.5 - [Save the fetched data from the external service to the database](https://github.com/frieZZerr/UJ-OOP/commit/db1de5a2eaa192f0c18820d58e1434b77ded219c)

:white_check_mark: 5.0 - [Extend the endpoint to handle more stocks, returning JSON](https://github.com/frieZZerr/UJ-OOP/commit/db1de5a2eaa192f0c18820d58e1434b77ded219c)

Code: [project_4](https://github.com/frieZZerr/UJ-OOP/tree/project_4)
