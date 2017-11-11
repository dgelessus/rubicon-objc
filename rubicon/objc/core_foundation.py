from ctypes import c_double, c_uint32, c_ulong, cdll, util

from .runtime import objc_id

__all__ = [
    'CFAbsoluteTime',
    'CFAllocatorRef',
    'CFArrayRef',
    'CFAttributedStringRef',
    'CFData',
    'CFDataRef',
    'CFDictionaryRef',
    'CFMutableArrayRef',
    'CFMutableDictionaryRef',
    'CFMutableSetRef',
    'CFNumberRef',
    'CFOptionFlags',
    'CFRunLoopRef',
    'CFSetRef',
    'CFStringEncoding',
    'CFStringRef',
    'CFTimeInterval',
    'CFTypeID',
    'CFTypeRef',
    'kCFAllocatorDefault',
    'kCFRunLoopDefaultMode',
    'kCFStringEncodingUTF8',
    'libcf',
]


######################################################################

# CORE FOUNDATION

libcf = cdll.LoadLibrary(util.find_library('CoreFoundation'))

CFTypeID = c_ulong

# Core Foundation type refs. These are all treated as equivalent to objc_id.

CFTypeRef = objc_id

CFAllocatorRef = objc_id
kCFAllocatorDefault = None

CFArrayRef = objc_id
CFAttributedStringRef = objc_id
CFData = objc_id
CFDataRef = objc_id
CFDictionaryRef = objc_id
CFMutableArrayRef = objc_id
CFMutableDictionaryRef = objc_id
CFMutableSetRef = objc_id
CFNumberRef = objc_id
CFOptionFlags = c_ulong
CFRunLoopRef = objc_id
CFSetRef = objc_id
CFStringRef = objc_id

CFStringEncoding = c_uint32
kCFStringEncodingUTF8 = 0x08000100

CFTimeInterval = c_double
CFAbsoluteTime = CFTimeInterval


kCFRunLoopDefaultMode = CFStringRef.in_dll(libcf, 'kCFRunLoopDefaultMode')

libcf.CFRunLoopGetCurrent.restype = CFRunLoopRef
libcf.CFRunLoopGetCurrent.argtypes = []

libcf.CFRunLoopGetMain.restype = CFRunLoopRef
libcf.CFRunLoopGetMain.argtypes = []
