# 🧠 IPAddress v2

**IPAddress v2** is an advanced and fully refactored version of the original *IPaddress* project, rewritten with enhanced architecture, improved logic flow, and modern coding practices.
Designed to be more than a simple IP resolver, this version introduces structural rigor, modularity, and maintainability while maintaining high performance and clean semantics.

---

![IP Address Banner](assets/ipaddres_banner_terminal.png)

---

## Overview

This project aims to provide a robust command-line tool for IP address resolution, network validation, and extended information retrieval.  
The design emphasizes software engineering best practices, ensuring code readability, scalability, and maintainability. Every component is carefully decoupled, following principles such as **single responsibility**, **dependency separation**, and **modular extensibility**.

Unlike basic implementations, **IPAddress v2** follows a strict layered logic that separates **core functionalities**, **data handling**, and **execution flow**, ensuring that future integrations (such as database logging, API support, or graphical output) can be added with minimal refactoring.

## Execution Example

```python
IP Geolocation - Python Edition
Enter IP address: 8.8.8.8

=== IP INFORMATION ===
Country: US
Region: California
City: Mountain View
Organization: AS15169 Google LLC
Postal Code: 94043
Coordinates: 37.4056, -122.0775
Google Maps: https://www.google.com/maps/?q=37.4056,-122.0775
```


## Core Features

- **Accurate IP Resolution:** Retrieves and validates both IPv4 and IPv6 addresses.  
- **Advanced Exception Handling:** Robust error handling to manage connection issues, invalid inputs, and unexpected responses.  
- **Modular Architecture:** Each operation (network request, parsing, validation, display) is handled by independent and testable components.  
- **Enhanced Output:** Clear, structured console output including ASCII banners and formatted results.  
- **Scalable Codebase:** Ready for extension with future features such as JSON export or API querying.  
- **Cross-Platform Execution:** Works seamlessly on Windows, Linux, and macOS environments.


## Code Design Philosophy

The project’s logic follows a clean, object-oriented approach inspired by modern development standards.  
Each component has a clearly defined purpose and does not interfere with other modules, resulting in a predictable and debuggable flow.

Key principles followed in the design:

- **Encapsulation:** Internal logic and data are isolated within each class or function.  
- **Abstraction:** Complex operations (e.g., data parsing, networking) are hidden behind clean method interfaces.  
- **Error Isolation:** All exceptions are caught and handled gracefully, avoiding unexpected termination.  
- **Readability First:** Variable names, method calls, and file structure are all human-readable and semantically meaningful.  
- **Consistency:** Uniform naming conventions, code comments, and logic patterns across the entire codebase.

## Logic Flow Description

When executed, the program initializes by loading configuration and environment parameters, then prints a stylized **ASCII banner** (as shown above).  
It then proceeds to:

1. **Capture or request the target IP address**  
2. **Validate** it using format recognition patterns  
3. **Query and process** the IP data through network lookups  
4. **Display results** in a formatted and readable layout  

Each operation is performed within a safe, encapsulated context to ensure that even unexpected behaviors are logged and managed gracefully.



