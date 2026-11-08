---
title: "Set Starting Page Number to 2 in Word"
date: 2021-09-14 06:49:58 +0000
author: "David Yang"
layout: post
categories: [programming-languages]
canonical: /starting-page-number-from-the-second-page-in-ms-word/
---

When you use the first page as a title or cover page, you typically want page numbering to start from the second page as “1”. Word makes this straightforward using the header/footer tools.

## Enable Different First Page Formatting

The first step is to tell Word to handle the first page differently from the rest of the document.

1.  Go to the **Insert** tab
2.  Select **Header & Footer** (or double-click in the header/footer area)
3.  In the **Options** group, check **Different First Page**

This separates the first page’s header and footer from all subsequent pages, letting you omit or customize the page number on the title page.

## Insert Page Numbers on Subsequent Pages

Once you’ve enabled different first page formatting:

1.  Click in the header or footer area of page 2 (the **first numbered page**)
2.  Go to **Insert** \> **Page Number**
3.  Choose your desired position (top of page, bottom of page, margins, etc.)

At this point, Word will show page numbers starting from “2” on your second page—because it’s counting from the actual page position.

## Start Numbering from 1 on Page 2

To make page 2 show as “1”, you need to adjust the page number format:

1.  Click on any page number field on page 2 or later
2.  Go to **Insert** \> **Page Number** \> **Format Page Numbers**
3.  In the **Page Number Format** dialog, set the **Start at** field to **0**

Now your second page will display as “1”, third page as “2”, and so on. The first page remains unnumbered since you enabled different first page formatting.

## Using Section Breaks for More Control

If you need finer control—for example, you have multiple sections with different numbering schemes—you can use section breaks instead:

1.  Place your cursor at the end of page 1
2.  Go to **Layout** \> **Breaks** \> **Next Page** (this creates a section break)
3.  On page 2, insert your page numbers as described above
4.  Right-click the page number field and select **Edit Field**
5.  In the Field dialog, check **Separate** under **Page Numbers** if you need to start numbering independently in this section

## Hiding the Page Number on the First Page Only

If you prefer not to use “Different First Page” but still want to hide the number on page 1 only:

1.  Insert page numbers normally across your document
2.  On the first page, double-click the page number field
3.  Right-click it and select **Edit Field**
4.  Add a conditional statement or simply delete the field from page 1 only

This approach gives you more flexibility if your first page layout doesn’t use a standard header or footer.

## Quick Troubleshooting

**Page numbers still showing as “2, 3, 4” on pages 2, 3, 4**: Make sure you clicked **Format Page Numbers** and set **Start at** to **0**, not **1**.

**Page number appears on the first page**: Verify that **Different First Page** is actually enabled. If you’re using a template, some may override this setting.

**Numbers are linked across pages**: If editing one page number affects others, you likely have a linked field. Click the page number and check if it’s an auto field or a manual insertion. Auto fields (inserted via Insert \> Page Number) automatically update across pages, which is usually what you want.
