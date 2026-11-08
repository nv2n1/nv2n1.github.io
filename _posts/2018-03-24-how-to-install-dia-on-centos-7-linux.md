---
title: "Installing Dia on CentOS 7"
date: 2018-03-24 11:51:27 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/how-to-install-dia-on-centos-7-linux/
---

Dia is a GTK+ based diagram creation program for Linux. It supports flowcharts, network diagrams, circuit diagrams, UML diagrams, and many other types. Here’s how to install and get started with Dia on CentOS 7.

## Install Dia from EPEL

Dia is available in the EPEL (Extra Packages for Enterprise Linux) repository:

```wp-block-code
# Enable EPEL if not already enabled
sudo yum install epel-release

# Install Dia
sudo yum install dia
```

After installation, launch it from the application menu or run `dia` in a terminal.

## Building Dia from Source

If the EPEL version is outdated or you need specific features, build from source:

```wp-block-code
# Install build dependencies
sudo yum groupinstall "Development Tools"
sudo yum install gtk2-devel libxml2-devel libxslt-devel gettext

# Download and build
wget https://ftp.gnome.org/pub/GNOME/sources/dia/0.97/dia-0.97.3.tar.xz
tar -xf dia-0.97.3.tar.xz
cd dia-0.97.3
./configure --enable-gnome
make
sudo make install
```

## Common Diagram Types

Dia includes built-in shape libraries for many diagram types:

- **Flowchart** — Process flows, decision trees, algorithm diagrams
- **UML** — Class diagrams, sequence diagrams, use case diagrams
- **Network** — Network topology, server racks, firewall layouts
- **Circuit** — Electrical and logic circuits
- **Database** — Entity-relationship diagrams
- **Sybase** — Database schema diagrams
- **GRAFCET** — Sequential function charts

## Basic Usage

**Creating a new diagram:**

1.  Launch Dia
2.  Select a sheet (diagram type) from the left panel
3.  Click a shape, then click on the canvas to place it
4.  Use the toolbox to connect shapes with lines and arrows

**Keyboard shortcuts:**

- `Ctrl+N` — New diagram
- `Ctrl+S` — Save diagram
- `Ctrl+E` — Export to another format
- `Ctrl+Z` — Undo
- `Delete` — Remove selected object
- `Ctrl+G` — Group selected objects
- `Ctrl+Shift+G` — Ungroup

## Exporting Diagrams

Dia can export to many formats:

```wp-block-code
# From the GUI: File -> Export
# Or from the command line:
dia --export=output.png --filter=png input.dia
dia --export=output.pdf --filter=pdf input.dia
dia --export=output.svg --filter=svg input.dia
```

Supported export formats include PNG, SVG, PDF, EPS, PostScript, WMF, Shape, and LaTeX PGF. For high-quality print output, use SVG or PDF rather than PNG.

## Custom Shapes

You can create custom shapes for Dia. A shape is defined in an XML file with a `.shape` extension:

```wp-block-code
~/.dia/shapes/my_custom.shape
```

Each shape file defines the geometry (SVG path), connection points, and text boxes. Place custom shapes in `~/.dia/shapes/` and they’ll appear in a new sheet in the toolbox.

## Alternatives to Dia

While Dia is functional, there are more modern diagramming tools available:

- **draw.io (diagrams.net)** — Web-based, free, excellent collaboration
- **LibreOffice Draw** — Part of the LibreOffice suite, good for general diagrams
- **Inkscape** — Vector graphics editor with diagramming capabilities
- **Mermaid** — Text-based diagram generation (integrates with Markdown)
- **PlantUML** — Text-based UML diagram generation

For quick network or flowchart diagrams, Dia remains a solid lightweight choice that doesn’t require an internet connection or modern web browser.

## Batch Processing with Dia

Dia supports command-line batch export, useful for automated documentation pipelines:

```wp-block-code
# Export all .dia files in a directory to PNG
for f in *.dia; do
    dia --export="${f%.dia}.png" --filter=png "$f"
done

# Export to SVG for web publishing
dia --export=diagram.svg --filter=svg diagram.dia

# Export to EPS for LaTeX documents
dia --export=diagram.eps --filter=eps diagram.dia
```

Integrate with documentation builds:

```wp-block-code
# Makefile snippet for docs
diagrams: $(patsubst %.dia,%.png,$(wildcard images/*.dia))

%.png: %.dia
    dia --export=$@ --filter=png $<
```

## Working with Dia Files Programmatically

Dia files are compressed XML. You can parse them directly:

```wp-block-code
# Decompress a .dia file
gunzip -c diagram.dia | xmllint --format - | less

# Extract all object types used
bunzip2 -c diagram.dia | grep 'type=' | sort -u
```

This makes Dia files suitable for version control (store the XML) and automated processing (count objects, validate diagram structure, generate reports).
