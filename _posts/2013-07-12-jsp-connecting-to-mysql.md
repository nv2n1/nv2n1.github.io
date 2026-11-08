---
title: "MySQL Database Connections in JSP: JDBC Setup and Connection Pooling"
date: 2013-07-12 16:47:40 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/jsp-connecting-to-mysql/
---

Connecting to MySQL from JSP requires the mysql-connector-j JDBC driver and proper connection handling. The old mysql-connector-java artifact is deprecated—switch to mysql-connector-j, which supports MySQL 8.0+ with modern SSL/TLS, authentication plugins, and performance improvements.

## Dependency Management

Add mysql-connector-j via Maven or Gradle. Maven is standard for modern Java projects:

``` xml
<dependency>
    <groupId>com.mysql</groupId>
    <artifactId>mysql-connector-j</artifactId>
    <version>8.4.0</version>
</dependency>
```

For Gradle:

``` gradle
dependencies {
    implementation 'com.mysql:mysql-connector-j:8.4.0'
}
```

If you’re managing dependencies manually, download the JAR from the MySQL website and place it in `WEB-INF/lib/`, then restart your application server.

## Direct Connections: Learning Only

This approach works but is unsuitable for production. Creating a new connection per request wastes resources, fails under load, and blocks threads waiting for connections:

``` jsp
<%@ page import="java.sql.*" %>
<%
    String driverName = "com.mysql.cj.jdbc.Driver";
    String url = "jdbc:mysql://localhost:3306/mydb?useSSL=true&serverTimezone=UTC";
    String username = "appuser";
    String password = "securepassword";

    Connection conn = null;
    Statement statement = null;
    ResultSet rs = null;

    try {
        Class.forName(driverName);
        conn = DriverManager.getConnection(url, username, password);
        statement = conn.createStatement();
        rs = statement.executeQuery("SELECT id, username FROM users LIMIT 10");

        while(rs.next()) {
            out.print(rs.getInt("id") + " | " + rs.getString("username") + "<br>");
        }
    } catch(SQLException e) {
        out.print("Error: " + e.getMessage());
    } finally {
        try {
            if(rs != null) rs.close();
            if(statement != null) statement.close();
            if(conn != null) conn.close();
        } catch(SQLException e) {
            e.printStackTrace();
        }
    }
%>
```

This is acceptable for educational purposes or trivial scripts, but don’t use it in any application handling real traffic.

## Connection Pooling with Tomcat JNDI

Connection pooling reuses connections across requests, eliminating the overhead of establishing new connections. Tomcat’s built-in pooling via JNDI is reliable and requires no additional dependencies.

Configure the datasource in `$CATALINA_BASE/conf/context.xml` or in an application-specific context file:

``` xml
<Context>
    <Resource name="jdbc/mydb"
              auth="Container"
              type="javax.sql.DataSource"
              driverClassName="com.mysql.cj.jdbc.Driver"
              url="jdbc:mysql://localhost:3306/mydb?useSSL=true&amp;serverTimezone=UTC&amp;cachePrepStmts=true&amp;prepStmtCacheSize=250&amp;socketTimeout=30000"
              username="appuser"
              password="securepassword"
              maxTotal="20"
              maxIdle="10"
              maxWaitMillis="30000"
              testOnBorrow="true"
              validationQuery="SELECT 1"/>
</Context>
```

Key attributes:

- `maxTotal`: Maximum connections in the pool (20 is reasonable for light to moderate traffic)
- `maxIdle`: Idle connections to keep open (reduces connection churn)
- `maxWaitMillis`: Milliseconds to wait before failing if no connection is available
- `testOnBorrow`: Validate connections before handing them out (catches stale connections)
- `validationQuery`: A lightweight query to test connection health

Reference this datasource in your `web.xml`:

``` xml
<resource-ref>
    <description>MySQL Datasource</description>
    <res-ref-name>jdbc/mydb</res-ref-name>
    <res-type>javax.sql.DataSource</res-type>
    <res-auth>Container</res-auth>
</resource-ref>
```

Access the pool from JSP:

``` jsp
<%@ page import="javax.sql.DataSource, javax.naming.InitialContext, java.sql.*" %>
<%
    try {
        InitialContext ctx = new InitialContext();
        DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/mydb");

        try(Connection conn = ds.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT username, email FROM users LIMIT 10")) {

            while(rs.next()) {
                out.print(rs.getString("username") + " | " + rs.getString("email") + "<br>");
            }
        }
    } catch(Exception e) {
        out.print("Error: " + e.getMessage());
    }
%>
```

The try-with-resources statement automatically closes the connection, statement, and result set, returning the connection to the pool for reuse.

## Prepared Statements and SQL Injection Prevention

Always use `PreparedStatement` when queries contain user input. This prevents SQL injection attacks and improves query plan caching:

``` jsp
<%@ page import="javax.sql.DataSource, javax.naming.InitialContext, java.sql.*" %>
<%
    String username = request.getParameter("username");

    try {
        InitialContext ctx = new InitialContext();
        DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/mydb");

        try(Connection conn = ds.getConnection()) {
            String sql = "SELECT id, email, created_at FROM users WHERE username = ?";

            try(PreparedStatement pstmt = conn.prepareStatement(sql)) {
                pstmt.setString(1, username);

                try(ResultSet rs = pstmt.executeQuery()) {
                    if(rs.next()) {
                        out.print("Email: " + rs.getString("email"));
                    } else {
                        out.print("User not found");
                    }
                }
            }
        }
    } catch(SQLException e) {
        out.print("Error: " + e.getMessage());
    }
%>
```

Never concatenate user input into SQL strings. Always use parameterized placeholders (`?`) and bind values via setter methods.

## Connection String Parameters

Include these in your JDBC URL for production stability:

- `useSSL=true`: Encrypt connections (required in production; false only for local dev)
- `serverTimezone=UTC`: Specify timezone explicitly; prevents ambiguity warnings
- `cachePrepStmts=true`: Cache prepared statement templates for better performance
- `prepStmtCacheSize=250`: Number of prepared statements to cache (tune based on your workload; 250 is sensible for most applications)
- `socketTimeout=30000`: Milliseconds before socket operations timeout (prevents hung connections)
- `allowPublicKeyRetrieval=true`: Required if using MySQL 8.0+ with default authentication plugin (only in development; use proper certificate setup in production)

Example URL with performance tuning:

    jdbc:mysql://localhost:3306/mydb?useSSL=true&serverTimezone=UTC&cachePrepStmts=true&prepStmtCacheSize=250&socketTimeout=30000

## Error Handling and Logging

Log database errors instead of printing them to response output. Direct error output exposes implementation details to clients:

``` jsp
<%@ page import="java.util.logging.*, javax.sql.DataSource, javax.naming.InitialContext, java.sql.*" %>
<%
    Logger logger = Logger.getLogger("myapp.database");

    try {
        InitialContext ctx = new InitialContext();
        DataSource ds = (DataSource) ctx.lookup("java:comp/env/jdbc/mydb");

        try(Connection conn = ds.getConnection()) {
            // database operations
        }
    } catch(SQLException e) {
        logger.log(Level.SEVERE, "Database connection failed", e);
        out.print("An error occurred. Please try again later.");
    }
%>
```

Use a proper logging framework like SLF4J with Logback in production rather than `java.util.logging`.

## Connection Pool Monitoring

Monitor your pool’s health in production. Tomcat exposes pool statistics via JMX. Check for:

- High `numActive` (connections in use): May indicate a connection leak or insufficient pool size
- Low `numIdle` (idle connections): Increase `maxTotal` if you’re regularly hitting limits
- High wait times: Increase pool size or optimize slow queries

Use a monitoring tool like Prometheus with the Tomcat JMX exporter to track these metrics over time.

## Alternative: HikariCP

For applications requiring advanced pooling features or better performance, use HikariCP instead of Tomcat’s pooling:

``` xml
<dependency>
    <groupId>com.zaxxer</groupId>
    <artifactId>HikariCP</artifactId>
    <version>5.1.0</version>
</dependency>
```

Configure HikariCP in a servlet context listener or initialization class, then store the `DataSource` in the application context for JSP access.

## Moving Beyond JSP

Embedding JDBC directly in JSP violates separation of concerns and makes code difficult to test. For new projects, use a framework like Spring Boot with Spring Data JPA, Hibernate, or Querydsl. These handle connection management, transaction control, and query building automatically.

If you must use JSP for legacy maintenance, isolate database access in a Data Access Object (DAO) layer and invoke it from servlets or controllers. This keeps views focused on rendering and business logic testable:

``` java
public class UserDAO {
    private DataSource dataSource;

    public UserDAO(DataSource ds) {
        this.dataSource = ds;
    }

    public List<User> getUsersByRole(String role) throws SQLException {
        String sql = "SELECT id, username, email FROM users WHERE role = ?";
        List<User> users = new ArrayList<>();

        try(Connection conn = dataSource.getConnection();
            PreparedStatement pstmt = conn.prepareStatement(sql)) {

            pstmt.setString(1, role);
            try(ResultSet rs = pstmt.executeQuery()) {
                while(rs.next()) {
                    users.add(new User(rs.getInt("id"), rs.getString("username"), rs.getString("email")));
                }
            }
        }
        return users;
    }
}
```

Then call the DAO from a servlet and forward the result to JSP for rendering.

## Summary

Use connection pooling for all production systems—either Tomcat’s built-in JNDI pooling or HikariCP. Always use `PreparedStatement` for any query with parameters. Enable SSL/TLS and proper timeout settings. Log errors rather than exposing them to clients. For new projects, avoid embedding JDBC in JSP; separate data access into a DAO layer or use a modern ORM framework.
