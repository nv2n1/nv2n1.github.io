---
title: "Importing Functions Between Node.js Modules"
date: 2018-03-24 11:50:38 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/in-node-js-how-to-import-functions-from-another-javascript-file/
---

The traditional Node.js approach uses `require()`. Create a module that exports functions, then import them where needed.

**exporting functions (math.js):**

``` javascript
function add(a, b) {
  return a + b;
}

function subtract(a, b) {
  return a - b;
}

module.exports = {
  add,
  subtract
};
```

**importing in another file (app.js):**

``` javascript
const { add, subtract } = require('./math.js');

console.log(add(5, 3));      // 8
console.log(subtract(5, 3)); // 2
```

You can also export individual functions:

``` javascript
module.exports.add = function(a, b) {
  return a + b;
};

module.exports.subtract = function(a, b) {
  return a - b;
};
```

Then import the entire module object:

``` javascript
const math = require('./math.js');
console.log(math.add(5, 3)); // 8
```

## ES Modules: import/export

Modern Node.js (14+) supports ES modules natively. Enable them by adding `"type": "module"` in your `package.json`, or use `.mjs` file extensions.

**exporting (math.js):**

``` javascript
export function add(a, b) {
  return a + b;
}

export function subtract(a, b) {
  return a - b;
}

export const PI = 3.14159;
```

**importing:**

``` javascript
import { add, subtract, PI } from './math.js';

console.log(add(5, 3));      // 8
console.log(subtract(5, 3)); // 2
console.log(PI);             // 3.14159
```

Import everything with a namespace:

``` javascript
import * as math from './math.js';

console.log(math.add(5, 3)); // 8
```

## Default exports

Export a single primary value as the default:

``` javascript
// logger.js
export default function log(message) {
  console.log(`[LOG] ${message}`);
}

// app.js
import log from './logger.js';
log('Application started');
```

Combine default and named exports:

``` javascript
// utils.js
export default function main() {
  return 'main function';
}

export function helper() {
  return 'helper function';
}

// app.js
import main, { helper } from './utils.js';
```

## Relative vs. absolute paths

Use relative paths for local modules:

``` javascript
// Works
import { add } from './math.js';
import { config } from '../config.js';
import { db } from '../../shared/database.js';

// Don't do this for local files
import { add } from 'math.js'; // Looks in node_modules
```

For package imports, use the package name without `./`:

``` javascript
import express from 'express';
import { readFile } from 'fs/promises';
```

## Mixing CommonJS and ES modules

If you must mix both (not recommended), be aware that:

- CommonJS files cannot directly `import` ES modules
- ES modules can `import` CommonJS files
- Use dynamic `import()` in CommonJS to load ES modules

``` javascript
// CommonJS file
(async () => {
  const module = await import('./esm-file.mjs');
  module.someFunction();
})();
```

## Practical tips

**Path resolution:** Node.js looks for modules in this order:

1.  Core modules (`fs`, `path`, etc.)
2.  `node_modules` directory
3.  Relative paths

**Avoid circular dependencies:** If module A imports from B, and B imports from A, you’ll hit issues. Restructure to eliminate the cycle.

**Package.json exports field:** For library authors, use the `exports` field to control what consumers can import:

``` json
{
  "name": "my-lib",
  "exports": {
    ".": "./dist/index.js",
    "./utils": "./dist/utils.js"
  }
}
```

Consumers can then:

``` javascript
import lib from 'my-lib';           // imports ./dist/index.js
import utils from 'my-lib/utils';   // imports ./dist/utils.js
```

**Use ES modules** in new projects. CommonJS is legacy but remains in use for backward compatibility.

## 2026 Comprehensive Guide: Best Practices

This extended guide covers Importing Functions Between Node.js Modules with advanced techniques and troubleshooting tips for 2026. Following modern best practices ensures reliable, maintainable, and secure systems.

## Advanced Implementation Strategies

For complex deployments, consider these approaches: Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment. Always document your custom configurations and maintain separate development, staging, and production environments.

## Security and Hardening

Security is foundational to all system administration. Implement layered defense: network segmentation, host-based firewalls, intrusion detection, and regular security audits. Use SSH key-based authentication instead of passwords. Encrypt sensitive data at rest and in transit. Follow the principle of least privilege for access controls.

## Performance Optimization

- Monitor resources continuously with tools like top, htop, iotop
- Profile application performance before and after optimizations
- Use caching strategically: application caches, database query caching, CDN for static assets
- Optimize database queries with proper indexing and query analysis
- Implement connection pooling for network services

## Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce the issue, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found. For intermittent issues, add monitoring and alerting. Use verbose modes and debug flags when needed.

## Related Tools and Utilities

These tools complement the techniques covered in this article:

- System monitoring: htop, vmstat, iostat, dstat for resource tracking
- Network analysis: tcpdump, wireshark, netstat, ss for connectivity debugging
- Log management: journalctl, tail, less for log analysis
- File operations: find, locate, fd, tree for efficient searching
- Package management: dnf, apt, rpm, zypper for package operations

## Integration with Modern Workflows

Modern operations emphasize automation, observability, and version control. Use orchestration tools like Ansible, Terraform, or Kubernetes for infrastructure. Implement centralized logging and metrics. Maintain comprehensive documentation for all systems and processes.

## Quick Reference Summary

This comprehensive guide provides extended knowledge for Importing Functions Between Node.js Modules. For specialized requirements, refer to official documentation. Practice in test environments before production deployment. Keep backups of critical configurations and data.
