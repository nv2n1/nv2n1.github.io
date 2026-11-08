---
title: "Configuring and Troubleshooting HP DesignJet Large-Format Printing"
date: 2015-03-28 02:48:36 +0000
layout: post
canonical: https://www.systutorials.com/how-to-print-powerpoint-poster-by-hp-designjet-500-plotter/
---

The HP DesignJet 500 and similar wide-format plotters handle posters, technical drawings, and large documents well—but they require careful configuration. This guide covers printing a 24″ × 36″ PowerPoint poster on a 36″ roll, though the process generalizes to other sizes.

## Understanding Your Hardware Constraints

The DesignJet 500 accepts roll media up to 36″ wide. For a 24″ × 36″ poster:

- **Roll width**: 36″ (your limiting factor)
- **Poster dimensions**: 24″ × 36″
- **Orientation**: Portrait with rotation
- **Print time**: 15–25 minutes at high quality
- **Media types supported**: Bond, coated, matte, glossy, fabric, vinyl

The roll width is your hard constraint—you can’t print wider than what’s loaded, and you must account for this in your document setup.

## Preparing Your Document

Before touching printer settings, ensure your PowerPoint slide is sized correctly:

1.  Go to **Design** → **Slide Size** (or **Page Setup** in older versions)
2.  Set custom dimensions to 24″ × 36″
3.  Review the slide in **Normal** or **Outline** view to verify text and images aren’t clustered at the edges
4.  Leave at least 0.25″ margins on all sides to account for plotter edge handling

## Configuring the Plotter

### Step 1: Access Printer Properties

1.  Open your presentation and navigate to **File** → **Print**
2.  Select the HP DesignJet 500 from the printer list
3.  Click **Properties** or **Printer Settings** (wording varies by OS)

### Step 2: Set Paper Size and Orientation

In the printer properties dialog:

- **Paper size**: Select “36 × 48 Roll” or the equivalent option for your roll width
- **Orientation**: Choose **Portrait**
- **Rotation**: Enable **Rotate 90 degrees**

This configuration places your 24″-wide poster correctly on the 36″ roll, with the 36″ dimension running along the feed direction. If the rotation option is grayed out, select a different paper size first, then return to your original choice.

### Step 3: Configure Output Quality and Media

Choose settings based on your use case:

**For presentation/marketing posters:**

- Print Quality: **Best** or **High**
- Color: **Color**
- Media Type: **Glossy** or **Coated Paper** (matches the roll loaded)

**For technical drawings or cost-conscious printing:**

- Print Quality: **Normal**
- Color: **Grayscale**
- Media Type: **Bond** or **Matte**

### Step 4: Verify Plotter Media Configuration

Before printing, confirm the physical roll loaded in the DesignJet matches your settings:

1.  Check the plotter’s **control panel** or **embedded web interface** (usually accessible at `http://<plotter-ip>`)
2.  Verify the roll width is set to 36″
3.  Confirm the media type matches your printer properties selection
4.  Check for any **jam indicators** or **media errors**

### Step 5: Print

Click **OK** and monitor the plotter’s progress. Large-format prints typically take 15–25 minutes depending on image complexity and quality settings.

## Troubleshooting

**Poster prints rotated incorrectly**

- Re-enable “Rotate 90 degrees” in orientation settings
- If the option is disabled, try selecting a different paper size, then revert to 36 × 48 Roll

**Poster gets cut off or scales unexpectedly**

- Verify the paper size in properties is 36 × 48 Roll (or matches your roll width exactly)
- Check that your PowerPoint slide dimensions are 24″ × 36″, not larger
- PowerPoint will auto-scale if it detects a mismatch between slide size and available print area

**Colors appear dull, faded, or inconsistent**

- Increase print quality from Normal to Best
- Verify media type in printer properties matches the loaded roll
- Run the plotter’s **color calibration** routine via its control panel or web interface
- Clean the print head: access maintenance via the control panel (typically under **Tools** → **Maintenance**)

**Plotter fails to feed media or produces jams**

- Ensure the roll is properly seated in both spindle holders
- Adjust the media guides to align with the 36″ roll width—guides too tight or loose will cause misfeeds
- Check the plotter’s error log via its web interface for specific fault codes
- Manually advance a small amount of media to clear potential jams before restarting

**Print quality degrades over time**

- Clean the print head every 50–100 prints or when colors start looking wrong
- Replace ink cartridges when low; running cartridges dry can damage nozzles
- Run a **nozzle check** before each critical print via the control panel

## Workflow Tips

**Create a saved printer preset** (if your PowerPoint version supports it) to avoid reconfiguring every time. Go to **File** → **Print** → **Print Layout** (or **Printer Settings**) and look for a **Save Settings** or **Presets** option.

**Always print a draft first**. Run one test copy at Normal quality to verify layout and colors before committing to a Best quality print, which uses more ink and time.

**Keep media on hand**. Large-format rolls are expensive but durable—test prints reveal issues before final versions, unlike single-use office paper.

**Maintain your plotter regularly**. Set a calendar reminder to clean the print head monthly and check for firmware updates quarterly via the web interface.

The DesignJet 500 delivers professional results once you nail the initial configuration. The setup effort on your first print establishes a reliable baseline for subsequent jobs.
