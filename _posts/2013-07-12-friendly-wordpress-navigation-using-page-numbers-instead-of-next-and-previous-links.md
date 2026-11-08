---
title: "Implementing Numbered Pagination in WordPress"
date: 2013-07-12 16:46:11 +0000
layout: post
canonical: https://www.systutorials.com/friendly-wordpress-navigation-using-page-numbers-instead-of-next-and-previous-links/
---

Numbered page navigation improves user experience and gives you better control over how visitors browse your content. Rather than forcing users through “previous/next” links, numbered pagination lets them jump directly to specific archive or search results pages.

## Why Use Numbered Pagination

**User Experience**: Visitors can skip directly to the page they need without clicking through sequentially. This matters when you have dozens of archive pages or search results spanning many pages.

**SEO Benefits**: Numbered pagination creates a tighter internal linking structure that helps search engines crawl and index your site’s content pages more effectively. It also signals the depth and organization of your content.

**Flexibility**: You control how many page links display and how pagination renders, making it easier to match your site’s design system.

## Basic Implementation

WordPress provides the `paginate_links()` function to handle numbered pagination. Create a file called `pagination.php` in your theme’s `template-parts` directory:

``` php
<?php
if ( ! defined( 'ABSPATH' ) ) {
    exit;
}

global $wp_query;

if ( $wp_query->max_num_pages <= 1 ) {
    return;
}

$paged = get_query_var( 'paged' ) ? get_query_var( 'paged' ) : 1;

// Build pagination base URL, respecting permalink structure
if ( get_option( 'permalink_structure' ) ) {
    $paginate_base = get_pagenum_link( 1 );
    if ( ! preg_match( '/\/$/', $paginate_base ) ) {
        $paginate_base .= '/';
    }
    $paginate_base .= 'page/%#%/';
} else {
    $paginate_base = add_query_arg( 'paged', '%#%' );
}

$pagination_args = array(
    'base'      => $paginate_base,
    'total'     => $wp_query->max_num_pages,
    'current'   => $paged,
    'mid_size'  => 2,
    'end_size'  => 1,
    'prev_text' => __( '&laquo; Previous', 'textdomain' ),
    'next_text' => __( 'Next &raquo;', 'textdomain' ),
    'type'      => 'list',
);

echo '<nav class="pagination" aria-label="' . esc_attr__( 'Posts navigation', 'textdomain' ) . '">';
echo paginate_links( $pagination_args );
echo '</nav>';
?>
```

Key points in this implementation:

- Checks `max_num_pages <= 1` to avoid displaying pagination when there’s only one page
- Uses `get_query_var()` to safely retrieve the current page number
- Respects your site’s permalink structure (with or without trailing slashes)
- Includes security checks with `ABSPATH` and proper escaping
- Uses `aria-label` for better accessibility instead of deprecated `role` attributes

## Styling Modern Pagination

Add this CSS to your theme’s stylesheet. It uses flexbox for responsive alignment:

``` css
.pagination {
    margin: 2rem 0;
    text-align: center;
}

.pagination ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.pagination li {
    margin: 0;
}

.pagination a,
.pagination span {
    display: inline-block;
    padding: 0.5rem 0.75rem;
    border: 1px solid #ddd;
    background: #fff;
    color: #333;
    text-decoration: none;
    border-radius: 4px;
    transition: background-color 0.2s, border-color 0.2s;
    font-weight: 500;
}

.pagination a:hover,
.pagination a:focus {
    background: #f5f5f5;
    border-color: #999;
    outline: 2px solid transparent;
    outline-offset: 2px;
}

.pagination .current {
    background: #333;
    color: #fff;
    border-color: #333;
    cursor: default;
}

.pagination .dots {
    padding: 0.5rem 0.25rem;
    border: none;
    color: #666;
}

/* Mobile responsive */
@media (max-width: 576px) {
    .pagination ul {
        gap: 0.25rem;
    }

    .pagination a,
    .pagination span {
        padding: 0.4rem 0.6rem;
        font-size: 0.9rem;
    }
}
```

## Adding Pagination to Your Templates

In your `index.php`, `archive.php`, and `search.php` templates, add pagination after your posts loop:

``` php
<?php
// After your posts loop ends
if ( have_posts() ) {
    while ( have_posts() ) {
        the_post();
        // Post content here
    }
}

get_template_part( 'template-parts/pagination' );
?>
```

The `get_template_part()` function is cleaner than direct includes and respects child theme overrides.

## Customizing Pagination Parameters

The main parameters you’ll adjust in `paginate_links()`:

- **mid_size**: Number of page links shown around the current page (default: 2). Set to 3 or higher for larger pagination blocks.
- **end_size**: Number of page links at the beginning and end (default: 1).
- **prev_text** / **next_text**: Customize previous/next button text. Use empty strings to hide them entirely.
- **type**: Use `'list'` for semantic HTML (recommended) or `'plain'` for just links.

Example for a minimal pagination that hides prev/next buttons:

``` php
$pagination_args = array(
    'base'      => $paginate_base,
    'total'     => $wp_query->max_num_pages,
    'current'   => $paged,
    'mid_size'  => 3,
    'end_size'  => 2,
    'prev_text' => '',
    'next_text' => '',
    'type'      => 'list',
);
```

## Custom Pagination Markup

For complete control over HTML structure, use `type => 'array'`:

``` php
$pages = paginate_links( array_merge( $pagination_args, array( 'type' => 'array' ) ) );

if ( $pages ) {
    echo '<nav class="pagination" aria-label="' . esc_attr__( 'Posts navigation', 'textdomain' ) . '">';
    echo '<ol>';
    foreach ( $pages as $page ) {
        echo '<li>' . $page . '</li>';
    }
    echo '</ol>';
    echo '</nav>';
}
```

This approach maintains WordPress’s pagination logic while letting you use semantic `<ol>` instead of `<ul>`, which is appropriate for numbered page lists.

## SEO Considerations

If you’re implementing pagination on archive pages, add rel links to your theme’s `<head>`:

``` php
<?php
if ( is_archive() || is_search() ) {
    if ( get_query_var( 'paged' ) > 1 ) {
        echo '<link rel="prev" href="' . esc_url( get_pagenum_link( get_query_var( 'paged' ) - 1 ) ) . '">';
    }
    if ( get_query_var( 'paged' ) < $wp_query->max_num_pages ) {
        echo '<link rel="next" href="' . esc_url( get_pagenum_link( get_query_var( 'paged' ) + 1 ) ) . '">';
    }
}
?>
```

These rel links help search engines understand the pagination structure and crawl through your archive pages more efficiently.
