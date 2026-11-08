---
title: "Configuring MediaWiki\u2019s Main Page: Redirects and Best Practices"
date: 2013-07-16 01:38:27 +0000
layout: post
canonical: https://www.systutorials.com/how-to-change-mediawikis-main-page-title-and-url/
---

MediaWiki stores its main page configuration in the `MediaWiki:Mainpage` system message. By default, this points to “Main Page”, but you can change it to any title that suits your wiki’s purpose. This process involves updating the system message, creating your new homepage, and handling redirects properly to avoid breaking external links and SEO.

## Step 1: Create Your New Main Page First

Before modifying any configuration, create the actual wiki page that will become your homepage. Navigate to your wiki and create a new page with your desired title (for example, “Welcome” or “Home”). Add all the content, sections, formatting, and templates your homepage needs. Save and verify the page renders correctly before proceeding.

## Step 2: Update the MediaWiki:Mainpage System Message

Log in with admin privileges and navigate directly to `MediaWiki:Mainpage` in your wiki. This is a special configuration page, not a regular article.

Click **Edit** and replace the entire content with your new main page title. If you want “Welcome” to be your homepage, the page should contain only:

    Welcome

The title must match exactly, including capitalization, with the actual wiki page you created. Save the changes immediately.

## Step 3: Handle the Old Main Page

Once your new main page is configured and live, decide what to do with the old “Main Page”.

### Option 1: Move with Redirect (Recommended)

This preserves external links and search engine rankings:

1.  Navigate to the old “Main Page”
2.  Click the dropdown menu next to **Edit** and select **Move**
3.  Enter a new title such as `Main Page/Archive` or `Archive/Old Main Page`
4.  Check the box labeled **Leave a redirect**
5.  Confirm the move

This creates a redirect from the old URL to your new main page, preserving any external links or search engine cache.

### Option 2: Delete

If the old main page contains no useful content and you have no external links to preserve, delete it instead:

1.  Navigate to the old “Main Page”
2.  Open the tools menu (or the dropdown next to **Edit**)
3.  Select **Delete** and confirm

Only use this option if you’re confident no external sites link to the old main page.

## Step 4: Check LocalSettings.php for Overrides

Some MediaWiki installations override the default main page behavior through configuration variables. Search your `LocalSettings.php` file for lines like:

``` php
$wgMainPageTitle = "Main Page";
```

If such a line exists, it will take precedence over your `MediaWiki:Mainpage` setting. Either remove it or update it to match your new main page title:

``` php
$wgMainPageTitle = "Welcome";
```

Restart any background services or clear your application cache if using one.

## Step 5: Update Internal References

Search your wiki for pages that hardcode references to “Main Page” in templates, transclusions, or navigation elements. Use the **Special:Search** page or the search function and look for:

- Pages linking to `[[Main Page]]`
- Templates that include `{% raw %}{{{% endraw %}MAINPAGENAME}}`
- Navigation boxes or sidebar configurations

Update these references to use your new main page title. If you use the `{% raw %}{{{% endraw %}MAINPAGENAME}}` magic word, it will automatically resolve to your new main page, so you may not need to change these.

## Step 6: Verify and Test

Clear your browser cache or open an incognito window and visit your wiki’s homepage. Confirm:

- Your new main page displays with the correct title
- All homepage navigation links work correctly
- Redirects function (if you created them)
- The page appears in search results with the correct title
- Special pages like `Special:Statistics` show the correct main page

For wikis indexed by search engines, the old main page URL (typically `index.php?title=Main_Page`) may remain cached in results for weeks. The redirect you created prevents 404 errors and gradually updates search engine indexes to the new page.

## Special Considerations

**Semantic MediaWiki users:** Verify that your main page configuration doesn’t conflict with namespace-specific settings or extension requirements. Test all primary workflows after making changes.

**Wiki farms:** If you manage multiple wikis, update the main page on each independently or use a shared configuration if your setup supports it.

**Mobile views:** Test your new main page on mobile browsers to ensure all content, navigation, and formatting display correctly on smaller screens.

**Interwiki links:** If external wikis link to your main page using interwiki syntax, those links will follow your redirect automatically.
