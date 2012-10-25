
def main():
    # Backup current qview settings
    try:
        shutil.rmtree(os.path.expandvars('$HOME/.Isis/qview.squishbackup'))
    except Exception:
        pass
    
    try:
        os.rename(os.path.expandvars('$HOME/.Isis/qview'), os.path.expandvars('$HOME/.Isis/qview.squishbackup'))
    except Exception:
        pass
    startApplication("qview")
    waitFor("object.exists(':File.&Open..._QAction')", 20000)
    test.compare(findObject(":File.&Open..._QAction").enabled, True)
    waitFor("object.exists(':File.&Browse..._QAction')", 20000)
    test.compare(findObject(":File.&Browse..._QAction").enabled, True)
    waitFor("object.exists(':File.&Save_QAction')", 20000)
    test.compare(findObject(":File.&Save_QAction").enabled, False)
    waitFor("object.exists(':File.Save &As..._QAction')", 20000)
    test.compare(findObject(":File.Save &As..._QAction").enabled, False)
    waitFor("object.exists(':File.Save &Info..._QAction')", 20000)
    test.compare(findObject(":File.Save &Info..._QAction").enabled, False)
    waitFor("object.exists(':File.Export View_QAction')", 20000)
    test.compare(findObject(":File.Export View_QAction").enabled, False)
    waitFor("object.exists(':File.&Print..._QAction')", 20000)
    test.compare(findObject(":File.&Print..._QAction").enabled, False)
    waitFor("object.exists(':File.&Close All..._QAction')", 20000)
    test.compare(findObject(":File.&Close All..._QAction").enabled, True)
    waitFor("object.exists(':File.E&xit_QAction')", 20000)
    test.compare(findObject(":File.E&xit_QAction").enabled, True)
    waitFor("object.exists(':View.&Fit in Window_QAction')", 20000)
    test.compare(findObject(":View.&Fit in Window_QAction").enabled, True)
    waitFor("object.exists(':View.&Actual Pixels_QAction')", 20000)
    test.compare(findObject(":View.&Actual Pixels_QAction").enabled, True)
    waitFor("object.exists(':View.Zoom In_QAction')", 20000)
    test.compare(findObject(":View.Zoom In_QAction").enabled, True)
    waitFor("object.exists(':View.Zoom Out_QAction')", 20000)
    test.compare(findObject(":View.Zoom Out_QAction").enabled, True)
    waitFor("object.exists(':View.&Pan Left_QAction')", 20000)
    test.compare(findObject(":View.&Pan Left_QAction").enabled, True)
    waitFor("object.exists(':View.&Pan Right_QAction')", 20000)
    test.compare(findObject(":View.&Pan Right_QAction").enabled, True)
    waitFor("object.exists(':View.&Pan Up_QAction')", 20000)
    test.compare(findObject(":View.&Pan Up_QAction").enabled, True)
    waitFor("object.exists(':View.&Pan Down_QAction')", 20000)
    test.compare(findObject(":View.&Pan Down_QAction").enabled, True)
    waitFor("object.exists(':View.Global Stretch_QAction')", 20000)
    test.compare(findObject(":View.Global Stretch_QAction").enabled, True)
    waitFor("object.exists(':View.Regional Stretch_QAction')", 20000)
    test.compare(findObject(":View.Regional Stretch_QAction").enabled, True)
    waitFor("object.exists(':Window.&Cascade_QAction')", 20000)
    test.compare(findObject(":Window.&Cascade_QAction").enabled, False)
    test.compare(findObject(":Window.&Cascade_QAction").checkable, False)
    waitFor("object.exists(':Window.&Tile_QAction')", 20000)
    test.compare(findObject(":Window.&Tile_QAction").enabled, False)
    test.compare(findObject(":Window.&Tile_QAction").checkable, False)
    waitFor("object.exists(':Window.Resize_QAction')", 20000)
    test.compare(findObject(":Window.Resize_QAction").checkable, False)
    test.compare(findObject(":Window.Resize_QAction").enabled, False)
    waitFor("object.exists(':Window.Change cursor to arrow._QAction')", 20000)
    test.compare(findObject(":Window.Change cursor to arrow._QAction").enabled, False)
    test.compare(findObject(":Window.Change cursor to arrow._QAction").text, "Change cursor to arrow.")
    test.compare(findObject(":Window.Change cursor to arrow._QAction").toolTip, "Change cursor to arrow.")
    test.compare(findObject(":Window.Change cursor to arrow._QAction").checkable, False)
    test.compare(findObject(":Window.Change cursor to arrow._QAction").whatsThis, "<b>Function: </b> Toggles the cursor shape between                                  and arrow and crosshair cursor when cursor is over the                                  viewport window.")
    waitFor("object.exists(':Window.&Next_QAction')", 20000)
    test.compare(findObject(":Window.&Next_QAction").enabled, False)
    test.compare(findObject(":Window.&Next_QAction").checkable, False)
    waitFor("object.exists(':Window.&Prev_QAction')", 20000)
    test.compare(findObject(":Window.&Prev_QAction").checkable, False)
    test.compare(findObject(":Window.&Prev_QAction").enabled, False)
    waitFor("object.exists(':Window.Close_QAction')", 20000)
    test.compare(findObject(":Window.Close_QAction").checkable, False)
    test.compare(findObject(":Window.Close_QAction").enabled, False)
    waitFor("object.exists(':Window.Close All_QAction')", 20000)
    test.compare(findObject(":Window.Close All_QAction").checkable, False)
    test.compare(findObject(":Window.Close All_QAction").enabled, False)
    waitFor("object.exists(':Window.&Link_QAction')", 20000)
    test.compare(findObject(":Window.&Link_QAction").checkable, True)
    test.compare(findObject(":Window.&Link_QAction").enabled, False)
    waitFor("object.exists(':Window.&Link All_QAction')", 20000)
    test.compare(findObject(":Window.&Link All_QAction").checkable, False)
    test.compare(findObject(":Window.&Link All_QAction").enabled, False)
    waitFor("object.exists(':Window.&Unlink All_QAction')", 20000)
    test.compare(findObject(":Window.&Unlink All_QAction").checkable, False)
    test.compare(findObject(":Window.&Unlink All_QAction").enabled, False)
    waitFor("object.exists(':Options.&Find Point_QAction')", 20000)
    test.compare(findObject(":Options.&Find Point_QAction").checkable, False)
    test.compare(findObject(":Options.&Find Point_QAction").enabled, False)
    waitFor("object.exists(':Options.&Blink ..._QAction')", 20000)
    test.compare(findObject(":Options.&Blink ..._QAction").checkable, False)
    test.compare(findObject(":Options.&Blink ..._QAction").enabled, False)
    waitFor("object.exists(':Options.Tracking ..._QAction')", 20000)
    test.compare(findObject(":Options.Tracking ..._QAction").enabled, True)
    test.compare(findObject(":Options.Tracking ..._QAction").checkable, False)
    waitFor("object.exists(':Options.Measuring ..._QAction')", 20000)
    test.compare(findObject(":Options.Measuring ..._QAction").checkable, False)
    test.compare(findObject(":Options.Measuring ..._QAction").enabled, True)
    waitFor("object.exists(':Options.Show Nomenclature_QAction')", 20000)
    test.compare(findObject(":Options.Show Nomenclature_QAction").checkable, True)
    test.compare(findObject(":Options.Show Nomenclature_QAction").enabled, True)
    waitFor("object.exists(':Options.&Special Pixel Tool ..._QAction')", 20000)
    test.compare(findObject(":Options.&Special Pixel Tool ..._QAction").checkable, False)
    test.compare(findObject(":Options.&Special Pixel Tool ..._QAction").enabled, False)
    waitFor("object.exists(':Sun Shadow Measurements_Isis::TableMainWindow')", 20000)
    test.compare(findObject(":Sun Shadow Measurements_Isis::TableMainWindow").visible, False)
    waitFor("object.exists(':Special Pixel Tool_QDialog')", 20000)
    test.compare(findObject(":Special Pixel Tool_QDialog").visible, False)
    waitFor("object.exists(':Statistics_QDialog')", 20000)
    test.compare(findObject(":Statistics_QDialog").visible, False)
    waitFor("object.exists(':Options.Registration_QMenu')", 20000)
    test.compare(findObject(":Options.Registration_QMenu").visible, False)
    waitFor("object.exists(':Measurements_Isis::TableMainWindow')", 20000)
    test.compare(findObject(":Measurements_Isis::TableMainWindow").visible, False)
    waitFor("object.exists(':qview_Isis::ViewportMainWindow')", 20000)
    test.compare(findObject(":qview_Isis::ViewportMainWindow").windowTitle, "qview")
    test.compare(findObject(":qview_Isis::ViewportMainWindow").enabled, True)
    test.compare(findObject(":qview_Isis::ViewportMainWindow").visible, True)
    waitFor("object.exists(':_Isis::AdvancedStretchDialog')", 20000)
    test.compare(findObject(":_Isis::AdvancedStretchDialog").visible, False)
    waitFor("object.exists(':Find Latitude/Longitude Coordinate_QDialog')", 20000)
    test.compare(findObject(":Find Latitude/Longitude Coordinate_QDialog").visible, False)

    waitFor("object.exists(':Elevation Calculator (via stereo pairs)_QMainWindow')", 20000)
    test.compare(findObject(":Elevation Calculator (via stereo pairs)_QMainWindow").visible, False)
    waitFor("object.exists(':Blink Comparator_QDialog')", 20000)
    test.compare(findObject(":Blink Comparator_QDialog").visible, False)
    waitFor("object.exists(':Advanced Tracking_Isis::TableMainWindow')", 20000)
    test.compare(findObject(":Advanced Tracking_Isis::TableMainWindow").visible, False)
    sendEvent("QCloseEvent", waitForObject(":qview_Isis::ViewportMainWindow"))
    
    # Restore original qview settings
    try:
        shutil.rmtree(os.path.expandvars('$HOME/.Isis/qview'))
    except Exception:
        pass
    
    try:
        os.rename(os.path.expandvars('$HOME/.Isis/qview.squishbackup'), os.path.expandvars('$HOME/.Isis/qview'))
    except Exception:
        pass
