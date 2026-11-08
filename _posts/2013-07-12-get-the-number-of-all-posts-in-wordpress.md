---
title: "Querying WordPress Posts by Type and Status"
date: 2013-07-12 16:46:12 +0000
author: "Eric Ma"
layout: post
canonical: https://www.systutorials.com/get-the-number-of-all-posts-in-wordpress/
---

The `wp_count_posts()` function returns a count object for any post type, making it essential for dashboards, theme displays, admin queries, and performance monitoring. Understanding how to use it correctly—and when to optimize—matters for WordPress development.

## Basic Usage

``` php
<?php
$count_posts = wp_count_posts();
$published = $count_posts->publish;
echo $published . " published posts";
?>
```

By default, `wp_count_posts()` counts posts. Pass a post type string to count other types:

``` php
<?php
$count_posts = wp_count_posts( 'post' );
$count_pages = wp_count_posts( 'page' );
$count_custom = wp_count_posts( 'my_custom_type' );

echo $count_posts->publish . " Posts, ";
echo $count_pages->publish . " Pages, ";
echo $count_custom->publish . " Custom Posts";
?>
```

## Post Status Properties

`wp_count_posts()` returns a `stdClass` object with these properties:

- **publish** — Published posts
- **draft** — Draft posts
- **pending** — Posts pending review
- **private** — Private posts
- **trash** — Trashed posts
- **auto-draft** — Auto-saved drafts
- **inherit** — Revision posts (typically for attachments)
- **future** — Scheduled posts

Access any status you need:

``` php
<?php
$counts = wp_count_posts( 'post' );
echo $counts->draft . " drafts, ";
echo $counts->pending . " pending, ";
echo $counts->future . " scheduled";
?>
```

## Counting Posts by Author

To count posts for a specific user, use `count_user_posts()`:

``` php
<?php
$user_posts = count_user_posts( get_current_user_id(), true );
echo "Current user has " . $user_posts . " posts";
?>
```

For more granular control with multiple filters, use `WP_Query`:

``` php
<?php
$args = array(
    'post_type'      => 'post',
    'post_status'    => 'publish',
    'author'         => get_current_user_id(),
    'posts_per_page' => -1,
);
$query = new WP_Query( $args );
echo "User published " . $query->found_posts . " posts";
wp_reset_postdata();
?>
```

`WP_Query` is slower than `wp_count_posts()` but allows filtering by additional parameters like date ranges, taxonomies, or meta values.

## Display in Templates

A common use case is showing post counts in navigation or sidebars:

``` php
<?php
$counts = wp_count_posts( 'post' );
$home_url = home_url();
?>
<ul>
  <li>
    <a href="<?php echo esc_url( $home_url ); ?>">
      <?php echo intval( $counts->publish ); ?> Posts
    </a>
  </li>
</ul>
```

Always escape output with `esc_url()`, `intval()`, or `esc_html()` to prevent security issues.

## Performance and Caching

`wp_count_posts()` queries the database and caches results at runtime. Accessing it repeatedly in loops degrades performance. Always cache the result in a variable:

``` php
<?php
$counts = wp_count_posts( 'post' );

// Reuse $counts multiple times
echo $counts->publish;
echo $counts->draft;
echo $counts->pending;
?>
```

For counting across many post types simultaneously, use a single database query instead of multiple function calls:

``` php
<?php
global $wpdb;
$results = $wpdb->get_results(
    "SELECT post_type, post_status, COUNT(*) as count 
     FROM {$wpdb->posts} 
     WHERE post_type IN ('post', 'page') 
     GROUP BY post_type, post_status"
);

foreach ( $results as $row ) {
    echo $row->post_type . " (" . $row->post_status . "): " . $row->count . "\n";
}
?>
```

Always use `$wpdb->prepare()` if filtering by user input to prevent SQL injection:

``` php
<?php
global $wpdb;
$post_type = 'post';
$results = $wpdb->get_results( $wpdb->prepare(
    "SELECT post_status, COUNT(*) as count FROM {$wpdb->posts} 
     WHERE post_type = %s GROUP BY post_status",
    $post_type
) );
?>
```

## Custom Post Types

Custom post types use the same function:

``` php
<?php
$product_counts = wp_count_posts( 'product' );
echo "Published products: " . $product_counts->publish;
?>
```

To list counts for all custom post types on your site:

``` php
<?php
$post_types = get_post_types( array( '_builtin' => false ), 'objects' );
foreach ( $post_types as $type ) {
    $counts = wp_count_posts( $type->name );
    echo $type->label . ": " . $counts->publish . "\n";
}
?>
```

This excludes built-in post types (posts, pages, attachments) and iterates only custom types, useful for multi-type dashboards or admin reports.
