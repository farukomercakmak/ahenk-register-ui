all: install

install: 
	mkdir -p $(DESTDIR)/usr/share/ahenk
	@cp -rf ahenk_register.py $(DESTDIR)/usr/share/ahenk/

	mkdir -p $(DESTDIR)/usr/share/ahenk
	@cp -rf icons $(DESTDIR)/usr/share/ahenk/

	mkdir -p $(DESTDIR)/usr/share/applications
	@cp -rf ahenk.desktop $(DESTDIR)/usr/share/applications/

uninstall:
	@rm -rf /usr/share/ahenk/ahenk_register.py
	@rm -rf /usr/share/applications/ahenk.desktop
	@rm -rf /usr/bin/ahenk/icons

.PHONY: install uninstall
