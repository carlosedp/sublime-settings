Sublime Text 3 settings

To use this repository, follow the steps below:

1. Download Sublime Text 3 from: https://www.sublimetext.com/3
2. Inside ST3, install "Package Manager" as the official documentation:

The simplest method of installation is through the Sublime Text console. The console is accessed via the ctrl+` shortcut or the View > Show Console menu. Once open, paste the appropriate Python code for your version of Sublime Text into the console.

    import urllib.request,os,hashlib; h = '6f4c264a24d933ce70df5dedcf1dcaee' + 'ebe013ee18cced0ef93d5f746d80ef60'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)

3. Find your local settings dir on the menu item: "Preferences -> Browse Packages"
4. Inside that dir, create or enter the "User" dir.
5. Unpack or checkout this repository into this dir making sure all the files are in the "User" directory and not in a "sublime-settings" dir. If needed, move the files.
6. Open Sublime Text and wait for it to install all the packages. 
7. On my settings I use a custom font that is included in the pack. Install it or change the config to one of your preference.
