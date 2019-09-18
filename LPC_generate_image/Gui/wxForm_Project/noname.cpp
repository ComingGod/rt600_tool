///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

MyFrame1::MyFrame1( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );

	wxBoxSizer* bSizerTop;
	bSizerTop = new wxBoxSizer( wxVERTICAL );

	wxWrapSizer* wSizer_Configuration;
	wSizer_Configuration = new wxWrapSizer( wxHORIZONTAL, wxWRAPSIZER_DEFAULT_FLAGS );

	m_notebook_configuration = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	m_panel_configuration = new wxPanel( m_notebook_configuration, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxGridSizer* gSizer_genImage;
	gSizer_genImage = new wxGridSizer( 0, 2, 0, 0 );

	m_staticText28 = new wxStaticText( m_panel_configuration, wxID_ANY, wxT("Input Image"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText28->Wrap( -1 );
	gSizer_genImage->Add( m_staticText28, 0, wxALL, 5 );

	m_textCtrl36 = new wxTextCtrl( m_panel_configuration, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer_genImage->Add( m_textCtrl36, 0, wxALL, 5 );

	m_staticText29 = new wxStaticText( m_panel_configuration, wxID_ANY, wxT("Image type"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText29->Wrap( -1 );
	gSizer_genImage->Add( m_staticText29, 0, wxALL, 5 );

	wxString m_choice_imageTypeChoices[] = { wxT("CRC"), wxT("Signed") };
	int m_choice_imageTypeNChoices = sizeof( m_choice_imageTypeChoices ) / sizeof( wxString );
	m_choice_imageType = new wxChoice( m_panel_configuration, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice_imageTypeNChoices, m_choice_imageTypeChoices, 0 );
	m_choice_imageType->SetSelection( 0 );
	gSizer_genImage->Add( m_choice_imageType, 0, wxALL, 5 );

	m_staticText30 = new wxStaticText( m_panel_configuration, wxID_ANY, wxT("LinkAddr"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText30->Wrap( -1 );
	gSizer_genImage->Add( m_staticText30, 0, wxALL, 5 );

	m_textCtrl38 = new wxTextCtrl( m_panel_configuration, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer_genImage->Add( m_textCtrl38, 0, wxALL, 5 );

	m_staticText31 = new wxStaticText( m_panel_configuration, wxID_ANY, wxT("EnableTrustZone"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText31->Wrap( -1 );
	gSizer_genImage->Add( m_staticText31, 0, wxALL, 5 );

	m_textCtrl39 = new wxTextCtrl( m_panel_configuration, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer_genImage->Add( m_textCtrl39, 0, wxALL, 5 );

	m_staticText32 = new wxStaticText( m_panel_configuration, wxID_ANY, wxT("MyLabel"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText32->Wrap( -1 );
	gSizer_genImage->Add( m_staticText32, 0, wxALL, 5 );

	m_textCtrl40 = new wxTextCtrl( m_panel_configuration, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer_genImage->Add( m_textCtrl40, 0, wxALL, 5 );

	m_button_genImage = new wxButton( m_panel_configuration, wxID_ANY, wxT("GenImage"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer_genImage->Add( m_button_genImage, 0, wxALL, 5 );


	m_panel_configuration->SetSizer( gSizer_genImage );
	m_panel_configuration->Layout();
	gSizer_genImage->Fit( m_panel_configuration );
	m_notebook_configuration->AddPage( m_panel_configuration, wxT("Gen Image"), false );

	wSizer_Configuration->Add( m_notebook_configuration, 1, wxEXPAND | wxALL, 5 );

	m_static_padding = new wxStaticText( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 70,-1 ), 0 );
	m_static_padding->Wrap( -1 );
	wSizer_Configuration->Add( m_static_padding, 0, wxALL, 5 );

	m_notebook29 = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	m_panel29 = new wxPanel( m_notebook29, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxGridSizer* gSizer11;
	gSizer11 = new wxGridSizer( 0, 2, 0, 0 );

	m_staticText48 = new wxStaticText( m_panel29, wxID_ANY, wxT("BootDevie"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText48->Wrap( -1 );
	gSizer11->Add( m_staticText48, 0, wxALL, 5 );

	wxString m_choice_bootDeviceChoices[] = { wxT("FlexspiNor"), wxT("Uart") };
	int m_choice_bootDeviceNChoices = sizeof( m_choice_bootDeviceChoices ) / sizeof( wxString );
	m_choice_bootDevice = new wxChoice( m_panel29, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_choice_bootDeviceNChoices, m_choice_bootDeviceChoices, 0 );
	m_choice_bootDevice->SetSelection( 0 );
	gSizer11->Add( m_choice_bootDevice, 0, wxALL, 5 );

	m_staticText49 = new wxStaticText( m_panel29, wxID_ANY, wxT("Option0"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText49->Wrap( -1 );
	gSizer11->Add( m_staticText49, 0, wxALL, 5 );

	m_textCtrl60 = new wxTextCtrl( m_panel29, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer11->Add( m_textCtrl60, 0, wxALL, 5 );

	m_staticText52 = new wxStaticText( m_panel29, wxID_ANY, wxT("Option1"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText52->Wrap( -1 );
	gSizer11->Add( m_staticText52, 0, wxALL, 5 );

	m_textCtrl64 = new wxTextCtrl( m_panel29, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer11->Add( m_textCtrl64, 0, wxALL, 5 );

	m_staticText53 = new wxStaticText( m_panel29, wxID_ANY, wxT("Fuse"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText53->Wrap( -1 );
	gSizer11->Add( m_staticText53, 0, wxALL, 5 );

	m_textCtrl65 = new wxTextCtrl( m_panel29, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer11->Add( m_textCtrl65, 0, wxALL, 5 );

	m_staticText54 = new wxStaticText( m_panel29, wxID_ANY, wxT("ComPort"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText54->Wrap( -1 );
	gSizer11->Add( m_staticText54, 0, wxALL, 5 );

	m_textCtrl_Comport = new wxTextCtrl( m_panel29, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	gSizer11->Add( m_textCtrl_Comport, 0, wxALL, 5 );

	m_button_download = new wxButton( m_panel29, wxID_ANY, wxT("Config"), wxDefaultPosition, wxDefaultSize, 0 );
	gSizer11->Add( m_button_download, 0, wxALL, 5 );


	m_panel29->SetSizer( gSizer11 );
	m_panel29->Layout();
	gSizer11->Fit( m_panel29 );
	m_notebook29->AddPage( m_panel29, wxT("Configuration"), false );

	wSizer_Configuration->Add( m_notebook29, 1, wxEXPAND | wxALL, 5 );


	bSizerTop->Add( wSizer_Configuration, 1, wxEXPAND, 5 );

	wxWrapSizer* wSizer_Log;
	wSizer_Log = new wxWrapSizer( wxHORIZONTAL, wxWRAPSIZER_DEFAULT_FLAGS );

	m_notebook26 = new wxNotebook( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, 0 );
	m_panel26 = new wxPanel( m_notebook26, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxTAB_TRAVERSAL );
	wxBoxSizer* bSizer29;
	bSizer29 = new wxBoxSizer( wxVERTICAL );

	m_textCtrl_Log = new wxTextCtrl( m_panel26, wxID_ANY, wxEmptyString, wxDefaultPosition, wxSize( 700,400 ), wxTE_MULTILINE );
	bSizer29->Add( m_textCtrl_Log, 0, wxALL, 5 );


	m_panel26->SetSizer( bSizer29 );
	m_panel26->Layout();
	bSizer29->Fit( m_panel26 );
	m_notebook26->AddPage( m_panel26, wxT("Log"), false );

	wSizer_Log->Add( m_notebook26, 1, wxEXPAND | wxALL, 5 );


	bSizerTop->Add( wSizer_Log, 1, wxEXPAND, 5 );


	this->SetSizer( bSizerTop );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_button_genImage->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::gen_image ), NULL, this );
	m_button_download->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::config_download ), NULL, this );
}

MyFrame1::~MyFrame1()
{
	// Disconnect Events
	m_button_genImage->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::gen_image ), NULL, this );
	m_button_download->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame1::config_download ), NULL, this );

}
