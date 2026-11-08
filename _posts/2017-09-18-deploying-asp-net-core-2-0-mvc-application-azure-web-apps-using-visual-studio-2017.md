---
title: "Deploy ASP.NET Core MVC Apps to Azure App Service"
date: 2017-09-18 13:11:58 +0000
layout: post
canonical: https://www.systutorials.com/deploying-asp-net-core-2-0-mvc-application-azure-web-apps-using-visual-studio-2017/
---

ASP.NET Core remains one of the most efficient frameworks for building scalable web applications. This guide walks through deploying an ASP.NET Core MVC application to Azure App Service using Visual Studio — the quickest path from local development to production.

## Prerequisites

You’ll need:

- An active Azure subscription (free tier accounts work fine for testing)
- Visual Studio 2022 or later with the Azure development workload installed
- .NET 8 or later SDK installed locally (LTS versions recommended)
- An Azure storage account or Application Insights configured (optional but recommended for monitoring)

Note: While this guide uses Visual Studio, you can also deploy via Azure CLI, GitHub Actions, or container deployment — choose based on your CI/CD pipeline.

## Creating the MVC Application

Open Visual Studio and create a new ASP.NET Core Web App project. Select the **Web App (Model-View-Controller)** template from the project type selection screen. Ensure you’re targeting a supported LTS .NET version (8 or later recommended for production stability).

The template generates a working MVC application with sample controllers and views. The project file (`*.csproj`) contains minimal dependencies — ASP.NET Core’s metapackage (`Microsoft.AspNetCore.App`) includes everything needed.

Before deployment, verify the application runs locally:

``` bash
dotnet run
```

Navigate to `https://localhost:5001` and confirm the default landing page appears without errors.

## Publishing to Azure App Service via Visual Studio

Right-click the project in Solution Explorer and select **Publish**.

The publish wizard opens. Choose **Azure** as the target, then select **Azure App Service (Windows)** or **Azure App Service (Linux)** depending on your preference. Linux deployments typically have lower costs and faster startup times.

Click **Create new** to provision a fresh App Service resource.

In the App Service creation dialog, configure:

- **App name**: Must be globally unique across Azure. This becomes your public URL (e.g., `appname.azurewebsites.net`)
- **Subscription**: Your Azure subscription
- **Resource Group**: Organize related resources. Create a new group or use an existing one
- **Hosting Plan**: Select an existing App Service Plan or create one. Start with **B1 (Basic)** for development; scale to **Standard** or **Premium** for production workloads
- **Application Insights**: Enable for monitoring application health and performance metrics

Leave other defaults unless you have specific requirements. Click **Create** — this may take 1–2 minutes.

Once provisioning completes, review the publish profile summary. The profile displays:

- Deployment method (Web Deploy)
- Site URL (publicly accessible)
- Options to manage or delete the profile

## Deploying the Application

The final screen shows deployment options. Click **Publish** to deploy your application to Azure.

Visual Studio streams deployment progress in the Web Publish Activity window. Watch for any build errors or authentication issues. Successful deployments end with the application opening in your default browser.

If the browser doesn’t open automatically, navigate directly to your app’s URL (e.g., `https://webmvcapp.azurewebsites.net`).

## Verifying Deployment in Azure Portal

Log into Azure Portal. Navigate to **App Services** in the left sidebar. Your newly created Web App appears in the list.

Click the app name to view its overview blade. Key information includes:

- **URL**: The public-facing address
- **Status**: Should show “Running”
- **Monitoring charts**: CPU, memory, and request metrics
- **Configuration**: Environment variables, connection strings, and app settings

Test the application by visiting its URL. The default MVC template displays without errors if deployment succeeded.

## Redeploying After Code Changes

Code updates deploy smoothly. Modify your application code locally — for example, change text in a controller or update a view:

``` csharp
public IActionResult Index()
{
    ViewData["Message"] = "Updated from Azure deployment";
    return View();
}
```

Commit and test locally:

``` bash
dotnet run
```

Return to Visual Studio’s Publish tab (or right-click project → **Publish** again). Review changed files using the Preview option if needed, then click **Publish**.

Deployments after the initial one are incremental — only changed files transfer. This completes in seconds to minutes depending on change scope. Refresh your browser to see updates live.

## Scaling and Production Considerations

For production workloads:

- **Enable HTTPS only** in App Service settings to force encrypted connections
- **Configure deployment slots** (Staging, Production) to test before switching traffic
- **Set Auto-scale rules** based on CPU or memory thresholds if you expect traffic spikes
- **Enable Application Insights** for detailed diagnostics and error tracking
- **Use Managed Identity** instead of connection string secrets for database access
- **Implement health checks** via the `/health` endpoint to ensure App Service restarts unhealthy instances
- **Set minimum instance count** to avoid cold starts on scaled-down apps
- **Configure custom domain names** with SSL/TLS certificates via Azure’s built-in or custom certificate support

## Continuous Deployment Alternative

For teams, configure continuous deployment via GitHub, Azure DevOps, or Bitbucket. App Service automatically redeploys when you push changes to your repository — eliminating manual publish steps entirely.

Configure this in Azure Portal under **Deployment Center** → select your repository → authorize and set the branch to deploy from.

This approach keeps your deployment pipeline code-centric: commits to main automatically trigger builds and deployments without touching Visual Studio’s publish interface.

## Troubleshooting Common Issues

**502 Bad Gateway errors** typically indicate the app failed to start. Check Application Insights logs or enable stdout logging:

In Azure Portal, navigate to **App Service logs** under the app’s settings and enable **Application logging (File System)** with level set to **Verbose**. View logs via the **Log stream** option.

**Slow deployments** may result from large dependency trees. Review the publish output in Visual Studio for long-running steps. Consider using deployment slots for zero-downtime updates on production apps.

**Connection string issues** after deployment commonly occur when environment-specific secrets aren’t configured. Store sensitive values in **Configuration** → **Application settings** rather than hardcoding them in `appsettings.json`.
