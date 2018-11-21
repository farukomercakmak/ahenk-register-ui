all: install

install:
	mkdir -p $(DESTDIR)/usr/share/ahenk-register
	@cp -rf ahenk-register.py $(DESTDIR)/usr/share/ahenk-register/
	@cp -rf icons $(DESTDIR)/usr/share/ahenk-register/

	mkdir -p $(DESTDIR)/usr/share/applications
	@cp -rf ahenk-register.desktop $(DESTDIR)/usr/share/applications/

	mkdir -p $(DESTDIR)/usr/bin
	@cp -rf ahenk-register $(DESTDIR)/usr/bin/

	mkdir -p $(DESTDIR)/usr/sbin
	@cp -rf ahenk-register-pkexec $(DESTDIR)/usr/sbin/

	mkdir -p $(DESTDIR)/usr/share/polkit-1/actions
	@cp -rf ahenk-register.policy $(DESTDIR)/usr/share/polkit-1/actions/

uninstall:
	@rm -rf /usr/share/ahenk-register/ahenk-register.py
	@rm -rf /usr/share/applications/ahenk-register.desktop
	@rm -rf /usr/bin/ahenk-register/icons
	@rm -rf /usr/bin/ahenk-register
	@rm -rf /usr/sbin/ahenk-register-pkexec
	@rm -rf /usr/share/polkit-1/actions/ahenk-register.policy
.PHONY: install uninstall
