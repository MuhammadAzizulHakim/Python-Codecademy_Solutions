garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
backwards = garbled[::-1]
message = backwards[::2]

print message
