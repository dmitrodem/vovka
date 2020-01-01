#!/usr/bin/env python3

import pcbnew
import sys
#board = pcbnew.GetBoard()
board = pcbnew.LoadBoard(sys.argv[1])

center = pcbnew.wxPoint(0, 0)

for drawing in board.GetDrawings():
    drawing.SetLayer(pcbnew.F_Cu)

    drawing_bottom = board.Duplicate(drawing, True)
    drawing_bottom = pcbnew.Cast_to_DRAWSEGMENT(pcbnew.Cast_to_BOARD_ITEM(drawing_bottom))
    drawing_bottom.Flip(center)
    
    mask = board.Duplicate(drawing, True)
    mask = pcbnew.Cast_to_DRAWSEGMENT(pcbnew.Cast_to_BOARD_ITEM(mask))
    mask.SetWidth(mask.GetWidth() + 200000*2)
    mask.SetLayer(pcbnew.F_Mask)

    mask_bottom = board.Duplicate(mask, True)
    mask_bottom = pcbnew.Cast_to_DRAWSEGMENT(pcbnew.Cast_to_BOARD_ITEM(mask_bottom))
    mask_bottom.Flip(center)

board.Save("/tmp/1.kicad_pcb")
