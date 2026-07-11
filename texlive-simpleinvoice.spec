%global tl_name simpleinvoice
%global tl_revision 45673

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Easy typesetting of invoices
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simpleinvoice
License:	gpl3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleinvoice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpleinvoice.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package lets you easily typeset professional-looking invoices. The
user specifies the content of the invoice by different \setPROPERTY
commands, and an invoice is generated automatically with the
\makeinvoice command.

