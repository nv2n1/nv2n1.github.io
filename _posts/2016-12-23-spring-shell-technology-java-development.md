---
title: "Building Java CLI Applications with Spring Shell 3.x"
date: 2016-12-23 13:16:48 +0000
author: "Johnnymorgan"
layout: post
categories: [languages-frameworks]
canonical: /spring-shell-technology-java-development/
---

Spring Shell is a framework for building command-line interfaces (CLIs) in Java applications. It provides structured command definition, argument parsing, tab completion, and history management—all integrated with the Spring ecosystem.

## Requirements and Setup

Spring Shell 3.2+ requires Java 17+ and Spring Boot 3.2+. If you’re still on older versions, Spring Shell 2.x supports Java 8 with Spring Framework 5.x, but migration is strongly recommended since 2.x is in maintenance mode.

### Starting with Spring Boot (Recommended)

Use the Spring Boot starter for the quickest setup. Add this to your `pom.xml`:

``` xml
<dependency>
    <groupId>org.springframework.shell</groupId>
    <artifactId>spring-shell-starter</artifactId>
    <version>3.2.0</version>
</dependency>
```

Or in `build.gradle`:

``` gradle
dependencies {
    implementation 'org.springframework.shell:spring-shell-starter:3.2.0'
}
```

The starter automatically configures Spring Shell beans and takes over your application’s main thread, launching an interactive shell on startup.

### Manual Configuration Without Spring Boot

If you’re using plain Spring Framework (not recommended), add these dependencies:

``` xml
<dependency>
    <groupId>org.springframework.shell</groupId>
    <artifactId>spring-shell-core</artifactId>
    <version>3.2.0</version>
</dependency>
<dependency>
    <groupId>org.springframework.context</groupId>
    <artifactId>spring-context</artifactId>
    <version>6.1.0</version>
</dependency>
```

You’ll need to manually instantiate and run the Shell bean, adding significant boilerplate. Use Spring Boot when possible.

## Defining Commands

Commands are methods annotated with `@CliCommand`. Use `@CliOption` to declare parameters and `@CliAvailabilityIndicator` to conditionally enable commands based on application state.

### Core Annotations

**@CliCommand** marks a method as an executable shell command:

``` java
@CliCommand(value = "greet", help = "Greet a user")
public String greetUser(
    @CliOption(key = "name", mandatory = true, help = "User's name") String name) {
    return "Hello, " + name + "!";
}
```

**@CliOption** defines command parameters with optional aliases and validation:

``` java
@CliOption(
    key = {"--verbose", "-v"},
    mandatory = false,
    help = "Enable verbose output"
)
boolean verbose
```

The `key` array allows multiple aliases for the same option (both `--verbose` and `-v` will work).

**@CliAvailabilityIndicator** conditionally enables/disables commands:

``` java
@CliAvailabilityIndicator(value = "admin-command")
public boolean isAdminAvailable() {
    return currentUser.hasAdminRole();
}
```

### Complete Command Implementation

``` java
@Component
public class UserCommand {

    @Autowired
    private UserService userService;

    @CliAvailabilityIndicator(value = "user-info")
    public boolean isUserInfoAvailable() {
        return true;
    }

    @CliCommand(value = "user-info", help = "Display user information")
    public String userInfo(
        @CliOption(
            key = "username",
            mandatory = true,
            help = "Username to look up"
        ) String username,
        @CliOption(
            key = {"--detailed", "-d"},
            mandatory = false,
            specifiedDefaultValue = "true",
            help = "Show detailed information"
        ) boolean detailed) {

        User user = userService.findByUsername(username);
        if (user == null) {
            return "Error: User '" + username + "' not found";
        }

        if (detailed) {
            return String.format("User: %s\nEmail: %s\nCreated: %s\nActive: %s",
                user.getUsername(),
                user.getEmail(),
                user.getCreatedDate(),
                user.isActive());
        }
        return String.format("User: %s (%s)", user.getUsername(), user.getEmail());
    }

    @CliCommand(value = "list-users", help = "List all users")
    public String listUsers() {
        return userService.findAll().stream()
            .map(User::getUsername)
            .collect(Collectors.joining("\n"));
    }
}
```

In Spring 3.x, the framework automatically detects command methods by annotation—no need to implement `CommandMarker`.

## Customizing Shell Appearance

### Custom Banner

Display a banner on startup:

``` java
@Component
@Order(Ordered.HIGHEST_PRECEDENCE)
public class CustomBannerProvider implements BannerProvider {

    @Override
    public String getProviderName() {
        return "Custom Shell";
    }

    @Override
    public String getBanner() {
        return "╔════════════════════════════════════╗\n" +
               "║     My Application Shell v1.0     ║\n" +
               "║  Type 'help' for available commands║\n" +
               "╚════════════════════════════════════╝\n";
    }

    @Override
    public String getWelcomeMessage() {
        return "Welcome to the shell application";
    }

    @Override
    public String getVersion() {
        return "1.0.0";
    }
}
```

### Custom Prompt and History

Control the shell prompt and history file location:

``` java
@Component
@Order(Ordered.HIGHEST_PRECEDENCE)
public class CustomPromptProvider implements PromptProvider {

    @Override
    public String getProviderName() {
        return "Custom Prompt";
    }

    @Override
    public String getPrompt() {
        return "myapp:> ";
    }

    @Override
    public String getHistoryFileName() {
        return ".myapp_history";
    }
}
```

The history file persists command history across sessions. Spring Shell loads previous commands automatically on startup.

## Building and Packaging

### Maven

Add the Spring Boot Maven plugin to create an executable JAR:

``` xml
<plugin>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-maven-plugin</artifactId>
    <version>3.2.0</version>
</plugin>
```

Build and run:

``` bash
mvn clean package
java -jar target/myapp-1.0.0.jar
```

### Gradle

Configure the Spring Boot plugin:

``` gradle
plugins {
    id 'java'
    id 'org.springframework.boot' version '3.2.0'
}

tasks.named('bootJar') {
    classifier = null
}
```

Build and run:

``` bash
gradle clean bootJar
java -jar build/libs/myapp-1.0.0.jar
```

## Interactive Shell Features

Once running, your shell supports:

- **Tab completion**: Press TAB to autocomplete commands and arguments
- **Help system**: Type `help` or `help <command>` for documentation
- **Command history**: Use arrow keys to navigate previous commands; persists across sessions
- **Clear screen**: Type `clear` to reset the terminal
- **Exit**: Type `exit` or `quit` to close the shell

## Input Validation and Error Handling

Spring Shell validates mandatory options automatically, but implement custom logic for complex cases:

``` java
@CliCommand(value = "process", help = "Process data")
public String processData(
    @CliOption(
        key = "file",
        mandatory = true,
        help = "Input file path"
    ) String filePath) {

    Path path = Paths.get(filePath);
    if (!Files.exists(path)) {
        return "Error: File not found - " + filePath;
    }

    try {
        return processFile(path);
    } catch (IOException e) {
        return "Error processing file: " + e.getMessage();
    }
}
```

For complex validation across multiple parameters, implement a `ParameterResolver` to intercept and validate arguments before they reach your command method.

## Practical Example: Background Job Trigger

A common use case is triggering asynchronous jobs from the shell:

``` java
@Component
public class JobCommand {

    @Autowired
    private JobScheduler jobScheduler;

    @CliCommand(value = "job trigger", help = "Trigger a scheduled job")
    public String triggerJob(
        @CliOption(
            key = "job-id",
            mandatory = true,
            help = "Job identifier"
        ) String jobId,
        @CliOption(
            key = {"--priority", "-p"},
            mandatory = false,
            specifiedDefaultValue = "NORMAL"
        ) String priority) {

        try {
            String taskId = jobScheduler.trigger(jobId, priority);
            return String.format("Job '%s' triggered (task: %s, priority: %s)", 
                jobId, taskId, priority);
        } catch (JobNotFoundException e) {
            return "Error: Job '" + jobId + "' not found";
        } catch (Exception e) {
            return "Error triggering job: " + e.getMessage();
        }
    }

    @CliCommand(value = "job status", help = "Check job execution status")
    public String jobStatus(
        @CliOption(key = "task-id", mandatory = true) String taskId) {
        return jobScheduler.getStatus(taskId);
    }

    @CliCommand(value = "job list", help = "List available jobs")
    public String listJobs() {
        return jobScheduler.listAvailable().stream()
            .map(job -> job.getId() + " - " + job.getDescription())
            .collect(Collectors.joining("\n"));
    }
}
```

## Testing Shell Commands

Use Spring Boot’s `@SpringBootTest` to test commands in isolation:

``` java
@SpringBootTest
class UserCommandTest {

    @Autowired
    private UserCommand userCommand;

    @MockBean
    private UserService userService;

    @Test
    void testUserInfo() {
        User testUser = new User("john", "john@example.com");
        when(userService.findByUsername("john")).thenReturn(testUser);

        String result = userCommand.userInfo("john", true);

        assertThat(result)
            .contains("john@example.com")
            .contains("john");
    }
}
```

Mock dependencies and invoke command methods directly to test behavior without running the full shell.

## Important Considerations

**Command Discovery**: Spring Shell scans the classpath for `@Component` beans with `@CliCommand` methods. If commands don’t appear, verify component scanning includes the package containing your commands.

**Thread Safety**: The shell runs commands on its main thread. For long-running operations, spawn them asynchronously and return status immediately—otherwise the shell will block until completion.

**Classpath Scanning**: Ensure your command beans are discoverable. Set `spring.application.name` in `application.properties` if component scanning doesn’t pick them up automatically.

**Exit Handling**: Override `CommandNotFound` or `ParsingException` beans if you need custom error messages for unknown commands or parsing failures.

Spring Shell eliminates the boilerplate of building CLIs—tab completion, history, argument parsing, and help all work out of the box. Focus on implementing your commands and let the framework handle the shell mechanics.
