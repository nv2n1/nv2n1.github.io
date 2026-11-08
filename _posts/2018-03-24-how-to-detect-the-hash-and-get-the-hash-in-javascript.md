---
title: "Detecting URL Hash Changes in JavaScript"
date: 2018-03-24 11:48:30 +0000
layout: post
canonical: https://www.systutorials.com/how-to-detect-the-hash-and-get-the-hash-in-javascript/
---

The URL hash — the fragment identifier after the `#` — serves several purposes: in-page navigation, client-side routing, and preserving application state. JavaScript provides straightforward APIs to read and monitor hash changes.

## Reading the Current Hash

Access the hash using `window.location.hash`:

``` javascript
const hash = window.location.hash;
console.log(hash); // e.g., "#section-about"
```

This returns the hash including the `#` character. To get the hash without the `#`:

``` javascript
const hash = window.location.hash.slice(1);
console.log(hash); // e.g., "section-about"
```

## Detecting Hash Changes

Use the `hashchange` event to respond when the URL fragment changes:

``` javascript
window.addEventListener('hashchange', (event) => {
  console.log('Old URL:', event.oldURL);
  console.log('New URL:', event.newURL);
  console.log('Current hash:', window.location.hash);
});
```

This fires when:

- A user clicks a link with an `href="#anchor"`
- The user uses browser back/forward buttons
- JavaScript programmatically changes the hash via `window.location.hash = '#new-hash'`

## Programmatically Changing the Hash

Modify the hash directly:

``` javascript
window.location.hash = '#section-contact';
```

Or use the History API for more control:

``` javascript
window.history.pushState(null, '', '#section-contact');
```

The `pushState` approach doesn’t trigger `hashchange`, so listen for `popstate` instead if you need to react to navigation:

``` javascript
window.addEventListener('popstate', (event) => {
  console.log('Navigated via back/forward');
});
```

## Practical Example: Simple Hash-Based Navigation

``` javascript
function handleNavigation() {
  const hash = window.location.hash.slice(1) || 'home';

  // Hide all sections
  document.querySelectorAll('[data-section]').forEach(el => {
    el.hidden = true;
  });

  // Show active section
  const activeSection = document.querySelector(`[data-section="${hash}"]`);
  if (activeSection) {
    activeSection.hidden = false;
  }
}

// Initialize on page load
handleNavigation();

// Listen for hash changes
window.addEventListener('hashchange', handleNavigation);
```

HTML structure:

``` html
<nav>
  <a href="#home">Home</a>
  <a href="#about">About</a>
  <a href="#contact">Contact</a>
</nav>

<section data-section="home">Home content</section>
<section data-section="about">About content</section>
<section data-section="contact">Contact content</section>
```

## When to Use Hashes vs. History API

**Use hashes** for:

- Simple single-page applications without a framework
- Static documentation sites with anchor-based navigation
- Backwards compatibility with older browsers (though hashes work in all modern browsers)

**Use the History API** (`pushState`/`replaceState`) for:

- Production SPAs with frameworks like React, Vue, or Svelte
- Cleaner URLs (e.g., `/about` instead of `/#/about`)
- More granular state management

Modern frameworks like Next.js, Nuxt, and SvelteKit handle routing automatically, so you rarely interact with the hash API directly in production. However, understanding these mechanics remains essential for simple projects, browser extensions, and debugging.

## Quick Reference

This article covered the essential concepts and commands for the topic. For more information, consult the official documentation or manual pages. The key takeaway is to understand the fundamentals before applying advanced configurations.

Practice in a test environment before making changes on production systems. Keep notes of what works and what does not for future reference.

## 2026 Best Practices

This article extends “Detecting URL Hash Changes in JavaScript” with practical guidance. Modern development practices emphasize security, performance, and maintainability. Follow these guidelines to build robust, production-ready systems.

## 2026 Comprehensive Guide for Bash

This article extends “Detecting URL Hash Changes in JavaScript” with advanced techniques and best practices for 2026. Following modern guidelines ensures reliable, maintainable, and secure systems.

### Advanced Implementation Strategies

For complex deployments involving bash, consider Infrastructure as Code for reproducible environments, container-based isolation for dependency management, and CI/CD pipelines for automated testing and deployment.

### Security and Hardening

Security should be built into workflows from the start. Use strong authentication methods, encrypt sensitive data, and follow the principle of least privilege for access controls.

### Performance Optimization

- Monitor system resources continuously with htop, vmstat, iotop
- Use caching strategies to optimize performance
- Profile application performance before and after optimizations
- Optimize database queries with proper indexing

### Troubleshooting Methodology

Follow a systematic approach to debugging: reproduce issues, isolate variables, check logs, test fixes. Keep detailed logs and document solutions found.

### Best Practices

- Write clean, self-documenting code with clear comments
- Use version control effectively with meaningful commit messages
- Implement proper testing before deployment
- Monitor production systems and set up alerts

### Resources and Further Reading

For more information on bash, consult official documentation and community resources. Stay updated with the latest tools and frameworks.
