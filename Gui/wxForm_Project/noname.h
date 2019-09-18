///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Oct 26 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/choice.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/sizer.h>
#include <wx/panel.h>
#include <wx/notebook.h>
#include <wx/wrapsizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame1
///////////////////////////////////////////////////////////////////////////////
class MyFrame1 : public wxFrame
{
	private:

	protected:
		wxNotebook* m_notebook_configuration;
		wxPanel* m_panel_configuration;
		wxStaticText* m_staticText28;
		wxTextCtrl* m_textCtrl36;
		wxStaticText* m_staticText29;
		wxChoice* m_choice_imageType;
		wxStaticText* m_staticText30;
		wxTextCtrl* m_textCtrl38;
		wxStaticText* m_staticText31;
		wxTextCtrl* m_textCtrl39;
		wxStaticText* m_staticText32;
		wxTextCtrl* m_textCtrl40;
		wxButton* m_button_genImage;
		wxStaticText* m_static_padding;
		wxNotebook* m_notebook29;
		wxPanel* m_panel29;
		wxStaticText* m_staticText48;
		wxChoice* m_choice_bootDevice;
		wxStaticText* m_staticText49;
		wxTextCtrl* m_textCtrl60;
		wxStaticText* m_staticText52;
		wxTextCtrl* m_textCtrl64;
		wxStaticText* m_staticText53;
		wxTextCtrl* m_textCtrl65;
		wxStaticText* m_staticText54;
		wxTextCtrl* m_textCtrl_Comport;
		wxButton* m_button_download;
		wxNotebook* m_notebook26;
		wxPanel* m_panel26;
		wxTextCtrl* m_textCtrl_Log;

		// Virtual event handlers, overide them in your derived class
		virtual void gen_image( wxCommandEvent& event ) { event.Skip(); }
		virtual void config_download( wxCommandEvent& event ) { event.Skip(); }


	public:

		MyFrame1( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("LPCTool"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 711,693 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MyFrame1();

};

