#pragma once

#define CFG_TUSB_RHPORT0_MODE   (OPT_MODE_DEVICE)

#define CFG_TUD_CDC 0
#define CFG_TUD_MSC 0
#define CFG_TUD_MIDI 1
#define CFG_TUD_VENDOR 0
#define CFG_TUD_XINPUT 4
// #define CFG_TUSB_DEBUG 1
// #define CFG_TUSB_DEBUG 2

// HID buffer size Should be sufficient to hold ID (if any) + Data
#define CFG_TUD_HID_EP_BUFSIZE 0x20
#define CFG_TUD_MIDI_TX_BUFSIZE 0x20
#define CFG_TUD_MIDI_RX_BUFSIZE 0x08
#define CFG_TUD_VENDOR_EP_BUFSIZE VENDOR_EPSIZE
#define CFG_TUD_VENDOR_TX_BUFSIZE VENDOR_EPSIZE
#define CFG_TUD_VENDOR_RX_BUFSIZE VENDOR_EPSIZE
#define CFG_TUD_XINPUT_TX_BUFSIZE 0x18
#define CFG_TUD_XINPUT_RX_BUFSIZE 0x08