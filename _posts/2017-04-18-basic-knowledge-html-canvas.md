---
title: "HTML5 Canvas: Drawing Graphics with JavaScript"
date: 2017-04-18 03:45:23 +0000
layout: post
canonical: https://www.systutorials.com/basic-knowledge-html-canvas/
---

The HTML5 `<canvas>` element lets you draw graphics programmatically using JavaScript. Unlike static images or SVG, canvas renders raster (bitmap) graphics directly to a 2D or 3D surface, making it ideal for animations, games, real-time visualizations, and interactive graphics that need frequent updates.

This guide covers canvas fundamentals and practical examples for sysadmins and developers who encounter canvas-based tools or need to troubleshoot canvas implementations.

## Canvas Element Basics

A canvas element is a container that requires JavaScript to draw anything:

``` html
<canvas id="myCanvas" width="800" height="600">
  Your browser does not support the canvas element.
</canvas>
```

Key attributes:

- `id` — Reference the canvas from JavaScript
- `width` and `height` — Canvas dimensions in pixels (defaults to 300×150 if omitted)
- Fallback text — Displays in browsers without canvas support (rare, but good practice)

**Important:** Set canvas dimensions using HTML `width` and `height` attributes, not CSS. CSS scaling distorts graphics and degrades performance by stretching the rendering context.

## Getting the Drawing Context

Canvas itself is just a container. All drawing happens through the Canvas API via JavaScript. You must retrieve the drawing context before any drawing:

``` javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// Now you can draw
ctx.fillStyle = 'blue';
ctx.fillRect(50, 50, 100, 100);
```

The `getContext()` method returns a context object that provides all drawing methods. You can also request `'webgl'` or `'webgl2'` for 3D graphics, but that’s beyond basic canvas.

## Drawing Shapes and Text

Here’s a practical example of common drawing operations:

``` javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');

// Filled rectangle
ctx.fillStyle = 'blue';
ctx.fillRect(50, 50, 100, 100);

// Rectangle outline
ctx.strokeStyle = 'green';
ctx.lineWidth = 2;
ctx.strokeRect(200, 50, 100, 100);

// Circle
ctx.beginPath();
ctx.arc(150, 200, 50, 0, Math.PI * 2);
ctx.fillStyle = 'red';
ctx.fill();

// Text
ctx.fillStyle = 'black';
ctx.font = 'bold 16px Arial';
ctx.fillText('Hello Canvas', 50, 300);
```

### Key Concepts

**Coordinate system:** Canvas uses (0,0) at the top-left, with x increasing rightward and y increasing downward.

**Paths:** Use `beginPath()` to start a new path, then `moveTo()`, `lineTo()`, `arc()`, and other methods to build shapes. Call `fill()` or `stroke()` to render.

**State management:** Canvas maintains drawing state (fill color, line width, font, opacity, transformations). Save and restore state to avoid side effects:

``` javascript
ctx.save();
ctx.fillStyle = 'blue';
ctx.globalAlpha = 0.5;
ctx.fillRect(0, 0, 100, 100);
ctx.restore();  // Restores fillStyle and globalAlpha
```

## Animation and Performance

For animations, use `requestAnimationFrame()` instead of `setInterval()`. It syncs with the browser’s refresh rate and is far more efficient:

``` javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
let x = 0;
const speed = 2;

function animate() {
  // Clear entire canvas
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  // Draw moving rectangle
  ctx.fillStyle = 'blue';
  ctx.fillRect(x, 50, 50, 50);

  // Update position
  x += speed;
  if (x > canvas.width) {
    x = -50;
  }

  requestAnimationFrame(animate);
}

animate();
```

### Performance Best Practices

- Use `requestAnimationFrame()` exclusively for animations—never mix with `setInterval()`.
- Clear only the regions you need to redraw, not the entire canvas (advanced optimization).
- Use offscreen canvases to pre-render or cache complex scenes.
- Consider WebGL for high-performance 3D graphics or very large datasets.
- Profile with browser DevTools to identify bottlenecks.

## Advanced Example: Interactive Particle Effect

``` javascript
const canvas = document.getElementById('myCanvas');
const ctx = canvas.getContext('2d');
const particles = [];

class Particle {
  constructor(x, y) {
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * 4;
    this.vy = (Math.random() - 0.5) * 4;
    this.alpha = 1;
    this.decay = 0.98;
  }

  update() {
    this.x += this.vx;
    this.y += this.vy;
    this.vy += 0.1;  // Gravity
    this.alpha *= this.decay;
  }

  draw(ctx) {
    ctx.globalAlpha = this.alpha;
    ctx.fillStyle = 'red';
    ctx.beginPath();
    ctx.arc(this.x, this.y, 5, 0, Math.PI * 2);
    ctx.fill();
    ctx.globalAlpha = 1;
  }
}

function animate() {
  ctx.fillStyle = 'white';
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  particles.forEach((p, i) => {
    p.update();
    p.draw(ctx);
    if (p.alpha < 0.01) particles.splice(i, 1);
  });

  requestAnimationFrame(animate);
}

// Click to spawn particles
canvas.addEventListener('click', (e) => {
  const rect = canvas.getBoundingClientRect();
  const x = e.clientX - rect.left;
  const y = e.clientY - rect.top;
  particles.push(new Particle(x, y));
});

animate();
```

## Canvas vs SVG

Choose the right tool for your use case:

| Feature       | Canvas                  | SVG                            |
|---------------|-------------------------|--------------------------------|
| Type          | Raster (bitmap)         | Vector                         |
| Scalability   | Fixed resolution        | Scales infinitely              |
| DOM           | Single element          | Full DOM tree                  |
| Performance   | Better for many objects | Better for few, complex shapes |
| Accessibility | Limited, requires ARIA  | Full semantic elements         |
| Editing       | Pixel-level only        | Elements are editable          |

**Use canvas for:**

- Games and interactive visualizations
- Real-time animated charts and graphs
- Image manipulation and filters
- Particle effects and visual effects

**Use SVG for:**

- Icons and logos
- Diagrams and flowcharts
- Responsive, scalable graphics
- Static or lightly interactive designs

## Debugging Canvas

Canvas can be opaque to debug since everything renders as pixels. Some tips:

- Use browser DevTools to inspect the canvas element and its attributes.
- Add temporary rectangles or text to verify coordinate calculations.
- Log values to the console during animation to track state changes.
- Enable the “Paint flashing” option in DevTools to see what areas redraw each frame.
- Test in multiple browsers—canvas behavior is generally consistent, but WebGL implementations vary.

Canvas is powerful for dynamic graphics, but it requires JavaScript to do anything. For static content, SVG or standard HTML is simpler and more accessible. Combine canvas with server-side tools (imagemagick, ffmpeg) when pre-rendering or batch processing images.
