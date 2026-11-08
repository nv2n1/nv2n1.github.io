---
title: "Custom WordPress Archives: Categories, Dates, and Posts"
date: 2013-07-12 16:46:10 +0000
layout: post
canonical: https://www.systutorials.com/put-the-categories-archives-and-all-posts-into-pages/
---

Consolidating categories, archives, and post listings into a dedicated page keeps your WordPress site structure clean and prevents search engines from treating navigation elements as content. Rather than scattering these across sidebar widgets, a dedicated archives page improves both user navigation and SEO by creating a single destination for content discovery.

## Create the Custom Page Template

WordPress doesn’t provide built-in templates for comprehensive archive displays, so you’ll create a custom page template. Add a new file to your theme directory — typically `wp-content/themes/your-theme/template-archives.php`:

``` php
<?php
/**
 * Template Name: Archives Page
 * Description: Displays categories, monthly archives, and all posts with pagination
 */

get_header();
?>

<div class="archives-container">
  <!-- Category section -->
  <section class="archives-section">
    <h2><?php esc_html_e( 'Categories', 'your-theme' ); ?></h2>
    <ul class="category-list">
      <?php wp_list_categories( array(
        'title_li'     => '',
        'show_count'   => 1,
        'hierarchical' => 1,
        'taxonomy'     => 'category',
      ) ); ?>
    </ul>
  </section>

  <!-- Archives section -->
  <section class="archives-section">
    <h2><?php esc_html_e( 'Archives by Month', 'your-theme' ); ?></h2>
    <ul class="archive-list">
      <?php wp_get_archives( array(
        'type'            => 'monthly',
        'show_post_count' => 1,
        'format'          => 'list',
      ) ); ?>
    </ul>
  </section>

  <!-- All posts section -->
  <section class="archives-section">
    <h2><?php esc_html_e( 'All Posts', 'your-theme' ); ?></h2>
    <ul class="posts-list">
      <?php
      $paged = get_query_var( 'paged' ) ? get_query_var( 'paged' ) : 1;
      $args  = array(
        'posts_per_page' => 50,
        'paged'          => $paged,
        'post_type'      => 'post',
        'post_status'    => 'publish',
        'orderby'        => 'date',
        'order'          => 'DESC',
      );
      $query = new WP_Query( $args );

      if ( $query->have_posts() ) {
        while ( $query->have_posts() ) {
          $query->the_post();
          ?>
          <li>
            <a href="<?php the_permalink(); ?>" title="<?php the_title_attribute(); ?>">
              <?php the_title(); ?>
            </a>
            <span class="post-date"><?php echo esc_html( get_the_date( 'F j, Y' ) ); ?></span>
          </li>
          <?php
        }

        // Pagination
        echo wp_kses_post( paginate_links( array(
          'total'   => $query->max_num_pages,
          'current' => $paged,
          'type'    => 'list',
          'mid_size' => 2,
          'prev_text' => esc_html__( '← Newer', 'your-theme' ),
          'next_text' => esc_html__( 'Older →', 'your-theme' ),
        ) ) );

        wp_reset_postdata();
      } else {
        echo '<li>' . esc_html__( 'No posts found.', 'your-theme' ) . '</li>';
      }
      ?>
    </ul>
  </section>
</div>

<?php get_footer(); ?>
```

After creating the template file, go to the WordPress admin, create a new page, and select “Archives Page” from the Template dropdown on the right sidebar.

## Display Categories with Post Counts

The `wp_list_categories()` function renders all categories with optional post counts. The `hierarchical` parameter preserves nested category relationships:

``` php
wp_list_categories( array(
  'title_li'     => '',              // Remove default <li> wrapper
  'show_count'   => 1,               // Show post count in parentheses
  'hierarchical' => 1,               // Show nested relationships
  'taxonomy'     => 'category',      // Explicitly specify taxonomy
  'exclude'      => '1,2,3',         // Exclude specific category IDs
  'depth'        => 1,               // Show only top-level categories
) );
```

Use `exclude` to hide specific categories (like “Uncategorized”). Set `depth=1` to display only top-level categories and suppress subcategories. For custom taxonomies, change `taxonomy` to your custom taxonomy slug.

## Display Archives by Time Period

The `wp_get_archives()` function organizes posts chronologically:

``` php
wp_get_archives( array(
  'type'            => 'monthly',    // yearly, daily, weekly, or monthly
  'show_post_count' => 1,            // Display post count
  'format'          => 'list',       // list or custom HTML
  'post_type'       => 'post',       // Optional: specify post type
) );
```

For a yearly archive view, use `'type' => 'yearly'`. This generates clickable links to archive pages automatically.

## List All Posts with Pagination

Always use `WP_Query` instead of the deprecated `query_posts()`. This approach scales efficiently, handles custom post types properly, and maintains the main loop state:

``` php
$paged = get_query_var( 'paged' ) ? get_query_var( 'paged' ) : 1;
$args  = array(
  'posts_per_page' => 50,
  'paged'          => $paged,
  'post_type'      => 'post',
  'post_status'    => 'publish',
  'orderby'        => 'date',
  'order'          => 'DESC',
  'suppress_filters' => false,       // Allow plugins to filter queries
);
$query = new WP_Query( $args );

if ( $query->have_posts() ) {
  while ( $query->have_posts() ) {
    $query->the_post();
    // Display post markup here
  }

  echo wp_kses_post( paginate_links( array(
    'total'     => $query->max_num_pages,
    'current'   => $paged,
    'type'      => 'list',
    'mid_size'  => 2,
    'prev_text' => esc_html__( '← Newer', 'your-theme' ),
    'next_text' => esc_html__( 'Older →', 'your-theme' ),
  ) ) );

  wp_reset_postdata();
}
```

Set `posts_per_page` to a reasonable number (50–100) to prevent memory issues on sites with thousands of posts. Always call `wp_reset_postdata()` after the loop to restore the main query state, which prevents template errors and plugin conflicts.

## Style the Archive Page

Use CSS Grid to create a responsive, multi-column layout:

``` css
.archives-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.archives-section {
  padding: 1.5rem;
  background: #f9f9f9;
  border-radius: 4px;
}

.archives-section h2 {
  border-bottom: 2px solid #333;
  padding-bottom: 0.5rem;
  margin: 0 0 1rem 0;
  font-size: 1.5rem;
}

.archives-section ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.archives-section li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #eee;
}

.archives-section li:last-child {
  border-bottom: none;
}

.archives-section a {
  color: #0073aa;
  text-decoration: none;
}

.archives-section a:hover {
  text-decoration: underline;
}

.posts-list .post-date {
  color: #666;
  font-size: 0.9rem;
  margin-left: 1rem;
  display: inline-block;
}

.page-numbers {
  display: flex;
  gap: 0.5rem;
  margin-top: 2rem;
  justify-content: center;
  flex-wrap: wrap;
}

.page-numbers a,
.page-numbers span {
  padding: 0.5rem 0.75rem;
  border: 1px solid #ddd;
  border-radius: 4px;
  text-decoration: none;
}

.page-numbers a:hover {
  background: #f0f0f0;
}

.page-numbers .current {
  background: #0073aa;
  color: #fff;
  border-color: #0073aa;
}

@media (max-width: 768px) {
  .archives-container {
    grid-template-columns: 1fr;
  }
}
```

## Caching for Performance

On sites with hundreds or thousands of posts, cache the archives output to reduce database queries:

``` php
$cache_key = 'archives_page_' . $paged;
$cached = wp_cache_get( $cache_key );

if ( $cached ) {
  echo $cached;
} else {
  ob_start();

  // Your query and output code here

  $output = ob_get_clean();
  wp_cache_set( $cache_key, $output, '', 3600 ); // Cache for 1 hour
  echo $output;
}
```

Use transients instead of `wp_cache_get()` if you need persistent caching across page refreshes:

``` php
$cache_key = 'archives_page_' . $paged;
$cached = get_transient( $cache_key );

if ( $cached ) {
  echo $cached;
} else {
  ob_start();
  // Query and output code
  $output = ob_get_clean();
  set_transient( $cache_key, $output, HOUR_IN_SECONDS );
  echo $output;
}
```

## Implementation Checklist

- Create `template-archives.php` in your theme directory
- Verify the Template Name comment is exactly as shown
- In WordPress admin, create a new page and select “Archives Page” from the template dropdown
- Publish the page and add it to your primary navigation menu
- Test pagination with at least 50 posts to verify correct page numbering
- Verify all category and archive links resolve without 404 errors
- Check that `wp_reset_postdata()` is called after the posts loop
- Add caching if your site has more than 500 posts
- Test on mobile to ensure the responsive grid layout works correctly

This approach gives visitors a single, comprehensive content hub while keeping archive pages separate from your main site structure, improving both SEO and page performance.
