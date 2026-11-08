---
title: "How to Add Custom Content to Receipts"
date: 2017-12-11 07:00:38 +0000
author: "jameswarner"
layout: post
categories: [development-best-practices]
canonical: /adding-customized-content-receipt/
---

When you need to display data on point-of-sale receipts that isn’t available in the standard receipt designer, you’ll need to create a custom field. This involves work in both Dynamics 365 (the backend) and the Retail SDK (the POS application layer).

This walkthrough covers adding a custom field—using item barcodes as an example—though the pattern applies to any custom receipt data.

## Step 1: Create the Custom Field in Dynamics 365

First, add the language text entry for your custom field.

Navigate to **Retail \> Setup \> Language text** and create a new entry. For our barcode example:

- **Language ID**: Your store’s language
- **Text ID**: A unique identifier (e.g., “ITEMBARCODE”)
- **Text**: Display label (e.g., “Item Barcode”)

Next, register the custom field itself. Go to **Retail \> Setup \> Custom fields** and create a new record:

- **Name**: A system name for the field
- **Type**: Select “Receipt”
- **Reference text ID**: Link to the language text entry you just created

Now open the receipt designer (**Retail \> Receipt setup \> Receipt designer**) and add your custom field to the appropriate section (header, lines, or footer). For line-item barcodes, add the field to the lines section.

After positioning the field, save the receipt. Run distribution job **1090** from the distribution schedule to push your customized receipt layout to the channel database.

## Step 2: Implement the Data Handler in Retail SDK

The Retail SDK’s Commerce Runtime (CRT) handles the business logic. You’ll need three classes: a Request class, a Response class, and a Handler class.

Create your Request class in the SDK’s data services project:

``` csharp
public class GetItemBarcodeRequest : Request
{
    public string ItemId { get; set; }
    public string InventDimId { get; set; }

    public GetItemBarcodeRequest(string itemId, string inventDimId)
    {
        this.ItemId = itemId;
        this.InventDimId = inventDimId;
    }
}
```

Create the Response class:

``` csharp
public class GetItemBarcodeResponse : Response
{
    public string ItemBarcode { get; set; }
}
```

Create the Handler class that executes the request and queries the database:

``` csharp
namespace Microsoft.Dynamics.Commerce.Runtime.DataServices
{
    public class GetItemBarcodeHandler : IRequestHandler
    {
        public IEnumerable<Type> SupportedRequestTypes
        {
            get { yield return typeof(GetItemBarcodeRequest); }
        }

        public Response Execute(Request request)
        {
            if (request == null)
            {
                throw new ArgumentNullException(nameof(request));
            }

            var barcodeRequest = request as GetItemBarcodeRequest;
            if (barcodeRequest == null)
            {
                throw new NotSupportedException($"Request type '{request.GetType()}' is not supported.");
            }

            return GetItemBarcode(barcodeRequest);
        }

        private GetItemBarcodeResponse GetItemBarcode(GetItemBarcodeRequest request)
        {
            if (string.IsNullOrEmpty(request.ItemId) || string.IsNullOrEmpty(request.InventDimId))
            {
                throw new ArgumentException("ItemId and InventDimId are required.");
            }

            var sqlContext = new SqlServerDatabaseContext(request.RequestContext);
            string barcode = QueryItemBarcode(request.ItemId, request.InventDimId, sqlContext);

            return new GetItemBarcodeResponse { ItemBarcode = barcode };
        }

        private string QueryItemBarcode(string itemId, string inventDimId, SqlServerDatabaseContext context)
        {
            var parameters = new ParameterSet
            {
                { "@ItemId", itemId },
                { "@InventDimId", inventDimId }
            };

            string query = @"
                SELECT ISNULL(ITEMBARCODE, 'None') as ITEMBARCODE
                FROM ax.INVENTITEMBARCODE
                WHERE ITEMID = @ItemId AND INVENTDIMID = @InventDimId";

            var sqlQuery = new SqlQuery(query, parameters);
            return context.ExecuteScalar<string>(sqlQuery) ?? "None";
        }
    }
}
```

Build this project and place the resulting DLL in the Retail Server’s bin folder.

## Step 3: Wire Up the Receipt Service

In the Retail SDK’s Services project, locate the `ReceiptService.cs` class and add a method to call your handler:

``` csharp
private static string GetItemBarcode(string itemId, string inventDimId, RequestContext context)
{
    var request = new GetItemBarcodeRequest(itemId, inventDimId);
    var response = context.Execute<GetItemBarcodeResponse>(request);

    return response?.ItemBarcode ?? "None";
}
```

In the `GetInfoFromSalesLineItem` method (which builds line-item data for receipts), call your new method:

``` csharp
public void GetInfoFromSalesLineItem(SalesLine line, RequestContext context)
{
    // ... existing code ...

    string barcode = GetItemBarcode(line.ItemId, line.InventoryDimensionId, context);
    // Map barcode to your custom receipt field
}
```

Rebuild the Services project and place the updated DLLs in the Retail Server bin folder.

## Deployment and Testing

After deploying the updated binaries:

1.  Restart the Retail Server
2.  Clear the browser cache on your POS device
3.  Restart Modern POS or Cloud POS
4.  Process a transaction and verify the custom field appears on the receipt

If the field doesn’t display, verify that:

- Both the data services and services DLLs are in the correct bin directory
- The receipt designer was properly updated and distribution job 1090 completed
- The Retail Server was restarted after deploying new binaries
- POS cache was cleared before reopening the application

This pattern works for any custom receipt field—adjust the SQL query and data mapping to fit your specific requirements.
