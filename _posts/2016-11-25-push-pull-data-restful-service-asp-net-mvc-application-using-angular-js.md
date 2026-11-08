---
title: "Building a REST API with ASP.NET MVC and JavaScript"
date: 2016-11-25 03:53:04 +0000
layout: post
canonical: https://www.systutorials.com/push-pull-data-restful-service-asp-net-mvc-application-using-angular-js/
---

This guide covers building REST endpoints in ASP.NET MVC and consuming them from a frontend application. While this example uses AngularJS (end-of-life 2022), the backend patterns remain relevant for legacy system maintenance. For new projects, migrate to ASP.NET Core with modern frontend frameworks like React, Vue, or Angular.

## Database Setup

Create the parts inventory table:

``` sql
CREATE TABLE [dbo].[PartMaster] (
    [Id] INT NOT NULL PRIMARY KEY IDENTITY(1,1),
    [PartNum] NVARCHAR(50) NOT NULL,
    [Name] NVARCHAR(MAX) NOT NULL,
    [Supplier] NVARCHAR(50) NULL,
    [Type] NCHAR(10) NULL
);

INSERT INTO PartMaster VALUES 
('P001', 'Alternator', 'Supplier A', 'Electrical'),
('P002', 'Battery', 'Supplier B', 'Electrical'),
('P003', 'Filter', 'Supplier C', 'Mechanical');
```

## ASP.NET MVC Controller Implementation

Build a controller that handles GET, POST, and DELETE operations with structured JSON responses:

``` csharp
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web.Mvc;

namespace MvcApplication.Controllers
{
    public class PartJsonController : Controller
    {
        public ActionResult Index()
        {
            return View();
        }

        [HttpGet]
        public JsonResult GetParts()
        {
            try
            {
                using (var context = new YourDbContext())
                {
                    var parts = context.PartMasters
                        .OrderBy(p => p.Id)
                        .ToList();
                    return Json(new { success = true, data = parts }, 
                        JsonRequestBehavior.AllowGet);
                }
            }
            catch (Exception ex)
            {
                return Json(new { success = false, message = ex.Message }, 
                    JsonRequestBehavior.AllowGet);
            }
        }

        [HttpPost]
        public JsonResult SavePart(PartMaster part)
        {
            if (!ModelState.IsValid)
            {
                var errors = ModelState.Values.SelectMany(v => v.Errors)
                    .Select(e => e.ErrorMessage);
                return Json(new { success = false, message = "Validation failed", errors = errors });
            }

            try
            {
                using (var context = new YourDbContext())
                {
                    if (part.Id == 0)
                    {
                        // New record
                        context.PartMasters.Add(part);
                    }
                    else
                    {
                        // Update existing record
                        var existing = context.PartMasters.Find(part.Id);
                        if (existing == null)
                            return Json(new { success = false, message = "Part not found" });

                        existing.PartNum = part.PartNum;
                        existing.Name = part.Name;
                        existing.Supplier = part.Supplier;
                        existing.Type = part.Type;
                    }

                    context.SaveChanges();
                    return Json(new { success = true, message = "Saved successfully", data = part });
                }
            }
            catch (DbUpdateException ex)
            {
                return Json(new { success = false, message = "Database error: " + ex.InnerException?.Message });
            }
            catch (Exception ex)
            {
                return Json(new { success = false, message = ex.Message });
            }
        }

        [HttpPost]
        public JsonResult DeletePart(int id)
        {
            try
            {
                using (var context = new YourDbContext())
                {
                    var part = context.PartMasters.Find(id);
                    if (part == null)
                        return Json(new { success = false, message = "Part not found" });

                    context.PartMasters.Remove(part);
                    context.SaveChanges();
                    return Json(new { success = true, message = "Deleted successfully" });
                }
            }
            catch (Exception ex)
            {
                return Json(new { success = false, message = ex.Message });
            }
        }
    }
}
```

### Key Implementation Details

- **Structured responses**: Always return `{ success: boolean, message: string, data?: any }` for consistent client-side handling
- **Database exceptions**: Catch `DbUpdateException` separately to distinguish constraint violations from other errors
- **Server-side validation**: Check `ModelState.IsValid` before processing to catch binding and data annotation errors
- **POST for mutations**: Use `[HttpPost]` instead of `[HttpDelete]` for better proxy compatibility in legacy environments
- **Error details**: Return error messages and validation error arrays to the client for appropriate UI feedback

## AngularJS Service and Controller

Create `Scripts/parts.controller.js`:

``` javascript
var PartModule = angular.module('PartMaintenance', ['ngAnimate', 'ngMessages']);

PartModule.controller('PartController', function($scope, $http, partService) {
    $scope.parts = [];
    $scope.currentPage = 1;
    $scope.pageSize = 10;
    $scope.totalItems = 0;
    $scope.sortField = 'name';
    $scope.sortReverse = false;
    $scope.searchFilter = {};
    $scope.loading = false;
    $scope.editingPart = null;
    $scope.errorMessage = '';
    $scope.successMessage = '';

    $scope.loadParts = function() {
        $scope.loading = true;
        partService.getParts().then(
            function(response) {
                if (response.data.success) {
                    $scope.parts = response.data.data || [];
                    $scope.totalItems = $scope.parts.length;
                    $scope.errorMessage = '';
                } else {
                    $scope.errorMessage = response.data.message || 'Failed to load parts';
                }
            },
            function(error) {
                $scope.errorMessage = 'Network error: ' + (error.statusText || 'Unknown');
                console.error('Error loading parts:', error);
            }
        ).finally(function() {
            $scope.loading = false;
        });
    };

    $scope.sortBy = function(field) {
        if ($scope.sortField === field) {
            $scope.sortReverse = !$scope.sortReverse;
        } else {
            $scope.sortField = field;
            $scope.sortReverse = false;
        }
    };

    $scope.savePart = function(part) {
        if (!part.partNum || !part.name) {
            $scope.errorMessage = 'Part Number and Name are required';
            return;
        }

        $scope.loading = true;
        partService.savePart(part).then(
            function(response) {
                if (response.data.success) {
                    $scope.successMessage = response.data.message;
                    $scope.errorMessage = '';
                    $scope.editingPart = null;
                    $scope.loadParts();
                    setTimeout(function() { 
                        $scope.$apply(function() { $scope.successMessage = ''; }); 
                    }, 3000);
                } else {
                    $scope.errorMessage = response.data.message || 'Failed to save';
                    if (response.data.errors) {
                        $scope.errorMessage += ': ' + response.data.errors.join(', ');
                    }
                }
            },
            function(error) {
                $scope.errorMessage = 'Network error while saving';
                console.error('Save error:', error);
            }
        ).finally(function() {
            $scope.loading = false;
        });
    };

    $scope.deletePart = function(id, partName) {
        if (!confirm('Delete "' + partName + '"? This cannot be undone.')) {
            return;
        }

        $scope.loading = true;
        partService.deletePart(id).then(
            function(response) {
                if (response.data.success) {
                    $scope.successMessage = response.data.message;
                    $scope.errorMessage = '';
                    $scope.loadParts();
                    setTimeout(function() { 
                        $scope.$apply(function() { $scope.successMessage = ''; }); 
                    }, 3000);
                } else {
                    $scope.errorMessage = response.data.message || 'Failed to delete';
                }
            },
            function(error) {
                $scope.errorMessage = 'Network error while deleting';
                console.error('Delete error:', error);
            }
        ).finally(function() {
            $scope.loading = false;
        });
    };

    $scope.editPart = function(part) {
        $scope.editingPart = angular.copy(part);
    };

    $scope.cancelEdit = function() {
        $scope.editingPart = null;
    };

    $scope.getDisplayedParts = function() {
        var filtered = $scope.parts.filter(function(part) {
            for (var key in $scope.searchFilter) {
                if ($scope.searchFilter[key] && 
                    !String(part[key]).toLowerCase().includes(String($scope.searchFilter[key]).toLowerCase())) {
                    return false;
                }
            }
            return true;
        });

        filtered.sort(function(a, b) {
            var aVal = a[$scope.sortField];
            var bVal = b[$scope.sortField];
            if (aVal < bVal) return $scope.sortReverse ? 1 : -1;
            if (aVal > bVal) return $scope.sortReverse ? -1 : 1;
            return 0;
        });

        var begin = ($scope.currentPage - 1) * $scope.pageSize;
        return filtered.slice(begin, begin + $scope.pageSize);
    };

    $scope.addNewPart = function() {
        $scope.editingPart = { id: 0, partNum: '', name: '', supplier: '', type: '' };
    };

    $scope.loadParts();
});

PartModule.factory('partService', function($http) {
    return {
        getParts: function() {
            return $http.get('/PartJson/GetParts');
        },
        savePart: function(part) {
            return $http.post('/PartJson/SavePart', part, {
                headers: { 'Content-Type': 'application/json' }
            });
        },
        deletePart: function(id) {
            return $http.post('/PartJson/DeletePart', { id: id }, {
                headers: { 'Content-Type': 'application/json' }
            });
        }
    };
});
```

### Service Layer Pattern

The `partService` factory abstracts HTTP calls and centralizes endpoint URLs. This pattern allows you to swap implementations or add request/response interceptors globally without modifying controller code.

## View Template

Create `Views/PartJson/Index.cshtml`:

``` html

@{
    ViewBag.Title = "Parts Management";
}

<h2>Parts Management</h2>

@section scripts {
    <script src="~/Scripts/angular.min.js"></script>
    <script src="~/Scripts/parts.controller.js"></script>
    <style>
        [ng-cloak] { display: none; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        .table-container { margin: 20px 0; }
        .table thead { background-color: #007bff; color: white; }
        .table th { cursor: pointer; user-select: none; }
        .table th:hover { background-color: #0056b3; }
        .sort-indicator { margin-left: 5px; font-size: 0.8em; }
        .search-row input { width: 100%; padding: 8px; margin: 5px 0; }
        .alert { margin: 15px 0; }
        .btn-group { display: flex; gap: 5px; }
        .modal-form { background: #f9f9f9; padding: 20px; border: 1px solid #ddd; margin: 20px 0; }
        .loading { opacity: 0.6; pointer-events: none; }
        .text-muted { color: #999; }
    </style>
}

<div ng-app="PartMaintenance" ng-controller="PartController" ng-cloak class="container">

    <!-- Messages -->
    <div ng-if="successMessage" class="alert alert-success" role="alert">
        {{successMessage}}
    </div>
    <div ng-if="errorMessage" class="alert alert-danger" role="alert">
        {{errorMessage}}
    </div>

    <!-- Add Part Button -->
    <div class="mb-3">
        <button class="btn btn-primary" ng-click="addNewPart()" ng-disabled="loading">
            <span ng-if="!loading">+ Add New Part</span>
            <span ng-if="loading">Loading...</span>
        </button>
    </div>

    <!-- Edit Form Modal -->
    <div ng-if="editingPart" class="modal-form">
        <h4>{{editingPart.id == 0 ? 'Add New Part' : 'Edit Part'}}</h4>
        <form name="partForm" ng-submit="savePart(editingPart)">
            <div class="form-row">
                <div class="form-group col-md-3">
                    <label>Part Number *</label>
                    <input type="text" class="form-control" ng-model="editingPart.partNum" required>
                </div>
                <div class="form-group col-md-4">
                    <label>Name *</label>
                    <input type="text" class="form-control" ng-model="editingPart.name" required>
                </div>
                <div class="form-group col-md-3">
                    <label>Supplier</label>
                    <input type="text" class="form-control" ng-model="editingPart.supplier">
                </div>
                <div class="form-group col-md-2">
                    <label>Type</label>
                    <input type="text" class="form-control" ng-model="editingPart.type">
                </div>
            </div>
            <button type="submit" class="btn btn-success" ng-disabled="loading">Save</button>
            <button type="button" class="btn btn-secondary" ng-click="cancelEdit()">Cancel</button>
        </form>
    </div>

    <!-- Parts Table -->
    <div class="table-container" ng-class="{ loading: loading }">
        <table class="table table-striped table-bordered table-hover">
            <thead>
                <tr>
                    <th ng-click="sortBy('id')">
                        ID <span class="sort-indicator" ng-if="sortField === 'id'">{{sortReverse ? '▼' : '▲'}}</span>
                    </th>
                    <th ng-click="sortBy('partNum')">
                        Part Number <span class="sort-indicator" ng-if="sortField === 'partNum'">{{sortReverse ? '▼' : '▲'}}</span>
                    </th>
                    <th ng-click="sortBy('name')">
                        Name <span class="sort-indicator" ng-if="sortField === 'name'">{{sortReverse ? '▼' : '▲'}}</span>
                    </th>
                    <th ng-click="sortBy('supplier')">
                        Supplier <span class="sort-indicator" ng-if="sortField === 'supplier'">{{sortReverse ? '▼' : '▲'}}</span>
                    </th>
                    <th ng-click="sortBy('type')">
                        Type <span class="sort-indicator"
```
