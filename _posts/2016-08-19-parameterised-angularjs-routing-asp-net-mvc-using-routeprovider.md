---
title: "Client-Side Routing in AngularJS: Managing Route Parameters"
date: 2016-08-19 08:04:42 +0000
layout: post
canonical: https://www.systutorials.com/parameterised-angularjs-routing-asp-net-mvc-using-routeprovider/
---

AngularJS routing enables single-page applications by dynamically switching views based on URL patterns without full page reloads. Unlike server-side routing, AngularJS handles routing on the client, eliminating network round-trips and improving responsiveness—particularly useful when displaying different datasets based on route parameters.

## Install AngularJS and Dependencies

Include AngularJS and the routing module. Using npm:

``` bash
npm install angular angular-route
```

For UI components, add Bootstrap:

``` bash
npm install bootstrap
```

Or via NuGet if working in a legacy .NET Framework environment:

``` powershell
Install-Package AngularJS.Core
Install-Package AngularJS.Route
Install-Package AngularJS.UI.Bootstrap
```

## Configure Script Bundles

Update `BundleConfig.cs` to include AngularJS and the routing module:

``` csharp
bundles.Add(new ScriptBundle("~/bundles/angular").Include(
    "~/Scripts/angular.min.js",
    "~/Scripts/angular-route.min.js",
    "~/Scripts/app/app.js",
    "~/Scripts/app/routes.js",
    "~/Scripts/app/controllers.js"
));
```

Register the bundle in `_Layout.cshtml`:

``` html
@Scripts.Render("~/bundles/angular")
```

## Define Routes with \$routeProvider

Create `Scripts/app/routes.js` to configure routing:

``` javascript
var mvcAngApp = angular.module('mvcAngApp', ['ngRoute']);

var configureRoutes = function ($routeProvider) {
    $routeProvider
        .when('/PartMaster/CPart', {
            templateUrl: '/PartMaster/Part/CustomerPart',
            controller: 'PartController',
            resolve: {
                parts: function ($http) {
                    return $http.get('/api/parts/customer')
                        .then(function (response) {
                            return response.data;
                        })
                        .catch(function (error) {
                            console.error('Failed to load customer parts:', error);
                            return [];
                        });
                }
            }
        })
        .when('/PartMaster/SPart', {
            templateUrl: '/PartMaster/Part/SupplierPart',
            controller: 'PartController',
            resolve: {
                parts: function ($http) {
                    return $http.get('/api/parts/supplier')
                        .then(function (response) {
                            return response.data;
                        });
                }
            }
        })
        .when('/PartMaster/SPart/:vendorId', {
            templateUrl: '/PartMaster/Part/SupplierPart',
            controller: 'PartController',
            resolve: {
                parts: function ($http, $route) {
                    var vendorId = $route.current.params.vendorId;
                    return $http.get('/api/parts/supplier', {
                        params: { vendorId: vendorId }
                    })
                        .then(function (response) {
                            return response.data;
                        })
                        .catch(function (error) {
                            console.error('Failed to load supplier parts:', error);
                            return [];
                        });
                }
            }
        })
        .otherwise({
            redirectTo: '/PartMaster/CPart'
        });
};

configureRoutes.$inject = ['$routeProvider'];
mvcAngApp.config(configureRoutes);
```

**Key points:**

- Use colon syntax (`:vendorId`) for route parameters
- The `templateUrl` property specifies which view to load
- Use `otherwise()` to provide a default route fallback
- Inject dependencies explicitly via `$inject` for minification safety
- The `resolve` property prevents controller activation until data loads, avoiding template rendering errors
- Always include `.catch()` handlers to display user-friendly error messages when data loads fail

## Create ASP.NET MVC Actions

Define controller actions that return partial views for each route. These should only return the partial view content, not a full HTML document:

``` csharp
[RoutePrefix("api/parts")]
public class PartsApiController : ApiController
{
    private PartDbContext db = new PartDbContext();

    [HttpGet]
    [Route("customer")]
    public IHttpActionResult GetCustomerParts()
    {
        var parts = db.PartMasters
            .Where(x => x.Type == "CPart")
            .ToList();
        return Ok(parts);
    }

    [HttpGet]
    [Route("supplier")]
    public IHttpActionResult GetSupplierParts(string vendorId = null)
    {
        var query = db.PartMasters
            .Where(x => x.Type == "SPart");

        if (!string.IsNullOrEmpty(vendorId))
        {
            query = query.Where(x => x.Supplier == vendorId);
        }

        return Ok(query.ToList());
    }
}
```

Create a corresponding MVC controller for view actions:

``` csharp
[RoutePrefix("PartMaster")]
public class PartMasterController : Controller
{
    [Route("Part/CustomerPart")]
    public ActionResult CustomerPartView()
    {
        return PartialView();
    }

    [Route("Part/SupplierPart")]
    public ActionResult SupplierPartView()
    {
        return PartialView();
    }
}
```

**Important:** Return `PartialView()` instead of `View()` to avoid rendering layout files. Separate API logic into a dedicated API controller (e.g., `PartsApiController`) using attribute routing with `/api/` prefix.

## Set Up the Main View

Add `ng-app` and `ng-view` to your main layout in `_Layout.cshtml`:

``` html
<div ng-app="mvcAngApp">
    <header>
        <!-- Navigation, header content -->
    </header>
    <div ng-view></div>
</div>
```

The `ng-view` directive is the placeholder where AngularJS injects routed templates.

## Create Partial Views

Create `Views/PartMaster/Part/CustomerPart.cshtml`:

``` html
<h2>Customer Parts</h2>
<div ng-if="!parts || parts.length === 0" class="alert alert-info">
    No customer parts found.
</div>
<table class="table table-striped" ng-if="parts && parts.length">
    <thead>
        <tr>
            <th>Part ID</th>
            <th>Part Name</th>
            <th>Type</th>
        </tr>
    </thead>
    <tbody>
        <tr ng-repeat="part in parts">
            <td>{{part.PartId}}</td>
            <td>{{part.PartName}}</td>
            <td>{{part.Type}}</td>
        </tr>
    </tbody>
</table>
```

Create `Views/PartMaster/Part/SupplierPart.cshtml` similarly:

``` html
<h2>Supplier Parts</h2>
<div ng-if="!parts || parts.length === 0" class="alert alert-info">
    No parts found for this supplier.
</div>
<table class="table table-striped" ng-if="parts && parts.length">
    <thead>
        <tr>
            <th>Part ID</th>
            <th>Part Name</th>
            <th>Supplier</th>
        </tr>
    </thead>
    <tbody>
        <tr ng-repeat="part in parts">
            <td>{{part.PartId}}</td>
            <td>{{part.PartName}}</td>
            <td>{{part.Supplier}}</td>
        </tr>
    </tbody>
</table>
```

Use `ng-if` for conditional rendering and add user-friendly messages when data is empty.

## Handle Route Parameters in Controllers

Create `Scripts/app/controllers.js`:

``` javascript
mvcAngApp.controller('PartController', function ($scope, $location, parts) {
    $scope.parts = parts;

    $scope.viewSupplierParts = function (vendorId) {
        $location.path('/PartMaster/SPart/' + vendorId);
    };

    $scope.$on('$destroy', function () {
        // Clean up subscriptions, timers, watchers
    });
});
```

The resolved `parts` data is automatically injected into the controller. Use `$location` for programmatic navigation.

## Navigation and Link Generation

Link to parameterized routes using `ng-href` to prevent broken links during parsing:

``` html
<a ng-href="#!/PartMaster/SPart/{{vendor.Id}}" class="btn btn-primary">
    View Parts for {{vendor.Name}}
</a>
```

The `#!` (hashbang) syntax ensures proper routing in older browsers. Use `ng-href` instead of `href` to avoid executing incomplete expressions.

## Performance Considerations

**Lazy loading:** Templates and data are loaded only when routes are accessed; the `resolve` property prevents controller activation until dependencies load.

**Template caching:** The `$templateCache` service automatically caches loaded templates after the first request, reducing subsequent network requests.

**Minification safety:** Always use the `$inject` array notation or inline array syntax to preserve dependency names during minification:

``` javascript
mvcAngApp.controller('PartController', ['$scope', '$location', 'parts', 
    function($scope, $location, parts) { }
]);
```

**Memory management:** Clean up watchers and listeners in `$destroy` events for long-lived applications:

``` javascript
$scope.$on('$destroy', function () {
    if (unsubscribe) unsubscribe();
    if (timer) clearTimeout(timer);
});
```

## Common Pitfalls

**Missing ng-app declaration:** AngularJS won’t bootstrap without it or will fail silently if placed after script execution.

**Parameter name mismatches:** Ensure parameter names in route definitions match those used in `$route.current.params`.

**Conflicting routes:** Avoid overlapping route patterns between ASP.NET MVC and AngularJS; use a dedicated namespace (e.g., `/api/`) for JSON endpoints and avoid routing collision.

**Returning full views instead of partials:** Always return `PartialView()` from actions called by `ng-view`, not `View()`.

**Missing error handling:** Add `.catch()` handlers to resolve promises to display user-friendly error messages:

``` javascript
resolve: {
    parts: function ($http, $q) {
        return $http.get('/api/parts/supplier')
            .catch(function (error) {
                console.error('Failed to load parts:', error);
                return $q.reject('Unable to load data. Please try again.');
            });
    }
}
```

**Unhandled rejections:** Always handle rejected promises to prevent console errors and silent failures.

## End-of-Life Considerations

AngularJS (1.x) reached end-of-life support in December 2021. While maintenance updates are no longer released, it remains functional for existing applications. For new projects, evaluate modern alternatives: **Angular 2+** offers better performance and type safety with TypeScript, **React** provides a component-based architecture with the largest ecosystem, or **Vue.js** offers a gentler learning curve for teams new to modern frameworks.

If maintaining AngularJS applications, prioritize security patches, monitor dependencies for vulnerabilities, and plan gradual migration strategies toward modern frameworks when feasible. Consider using tools like Webpack for bundling and module management to extend the lifespan of AngularJS codebases.
