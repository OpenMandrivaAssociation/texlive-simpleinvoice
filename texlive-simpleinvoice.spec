Name:		texlive-simpleinvoice
Version:	45673
Release:	2
Summary:	Easy typesetting of invoices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simpleinvoice
License:	gpl3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleinvoice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleinvoice.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package lets you easily typeset professional-looking
invoices. The user specifies the content of the invoice by
different \setPROPERTY commands, and an invoice is generated
automatically with the \makeinvoice command.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simpleinvoice
%doc %{_texmfdistdir}/doc/latex/simpleinvoice

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
