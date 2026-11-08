---
title: "Reading Environment Variables in Java"
date: 2018-03-24 11:52:13 +0000
modified: 2026-04-11 17:13:21 +0000
author: "Q A"
layout: post
categories: [languages-frameworks]
canonical: /how-to-get-an-environment-variable-in-java/
---

There are two primary ways to access environment variables in Java: `System.getenv()` for reading variables and `System.getProperty()` for reading system properties. They’re different things, so understanding which one you need matters.

### Reading Environment Variables with System.getenv()

`System.getenv()` retrieves variables set in your shell or container environment:

``` java
String javaHome = System.getenv("JAVA_HOME");
System.out.println("JAVA_HOME: " + javaHome);
```

To get all environment variables as a map:

``` java
Map<String, String> env = System.getenv();
env.forEach((key, value) -> System.out.println(key + " = " + value));
```

Check if a variable exists before accessing it to avoid null pointer exceptions:

``` java
String dbUrl = System.getenv("DATABASE_URL");
if (dbUrl != null) {
    // Use dbUrl
} else {
    throw new IllegalStateException("DATABASE_URL not set");
}
```

Or use `getOrDefault()` if you’re using a custom wrapper:

``` java
String port = System.getenv("APP_PORT");
int portNumber = Integer.parseInt(port != null ? port : "8080");
```

### Reading System Properties with System.getProperty()

System properties are different from environment variables. They’re set via `-D` flags at JVM startup:

``` java
String javaVersion = System.getProperty("java.version");
String osName = System.getProperty("os.name");
String userHome = System.getProperty("user.home");
```

Launch with custom properties:

``` bash
java -Dapp.environment=production -Dapp.name=myapp MyApplication
```

Then access them:

``` java
String environment = System.getProperty("app.environment");
String appName = System.getProperty("app.name");
```

### Spring Boot and ConfigurationProperties

In Spring Boot 3.x applications, the recommended approach is using `@ConfigurationProperties` or `@Value` annotations, which bind environment variables automatically:

``` java
@Configuration
@ConfigurationProperties(prefix = "app")
public class AppConfig {
    private String environment;
    private String databaseUrl;

    // Getters and setters
}
```

Or inject directly:

``` java
@Component
public class MyService {
    @Value("${DATABASE_URL:localhost}")
    private String databaseUrl;
}
```

Environment variables are converted to property names by replacing underscores with dots and lowercasing: `DATABASE_URL` becomes `database-url` or `database_url`.

### Working with Docker and Containerized Environments

When running in Docker, pass environment variables in your compose file or command:

``` bash
docker run -e DATABASE_URL=postgres://localhost -e APP_PORT=9000 myapp:latest
```

Or in `docker-compose.yml`:

``` yaml
services:
  app:
    image: myapp:latest
    environment:
      - DATABASE_URL=postgres://db:5432/mydb
      - APP_PORT=9000
      - LOG_LEVEL=INFO
```

Inside your Java app, read them normally with `System.getenv()`.

### Security Considerations

Never log sensitive environment variables (API keys, passwords, database credentials). If you need to debug configuration:

``` java
System.getenv().forEach((key, value) -> {
    if (!key.contains("PASSWORD") && !key.contains("TOKEN") && !key.contains("SECRET")) {
        System.out.println(key + " = " + value);
    }
});
```

Use secrets management tools in production:

- **Kubernetes**: Mount secrets as environment variables or files
- **Docker Swarm**: Use secret objects
- **Cloud platforms**: Use AWS Secrets Manager, Azure Key Vault, or GCP Secret Manager

Avoid hardcoding defaults for secrets in your application code. Always require explicit configuration in sensitive environments.

### Null Safety and Error Handling

Environment variables may not be set. Handle gracefully:

``` java
String required = System.getenv("REQUIRED_VAR");
if (required == null) {
    throw new IllegalStateException("REQUIRED_VAR environment variable must be set");
}

String optional = System.getenv("OPTIONAL_VAR");
String value = optional != null ? optional : "default-value";
```

For parsing numeric values, catch `NumberFormatException`:

``` java
String portStr = System.getenv("PORT");
int port = 8080;
if (portStr != null) {
    try {
        port = Integer.parseInt(portStr);
    } catch (NumberFormatException e) {
        throw new IllegalStateException("PORT must be a valid integer, got: " + portStr);
    }
}
```

Use environment variables for configuration that changes between deployments. Use system properties for JVM tuning flags and internal behavior. In Spring Boot applications, rely on `@ConfigurationProperties` for cleaner, type-safe configuration management.
