<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Capstone</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>




<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>



<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/*
 * Webkit scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-corner {
  background: var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-thumb {
  background: rgb(var(--jp-scrollbar-thumb-color));
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-right: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

[data-jp-theme-scrollbars='true'] ::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
  border-bottom: var(--jp-scrollbar-endpad) solid
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar */

[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar::-webkit-scrollbar,
[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-corner,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-corner {
  background-color: transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-thumb,
[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
  border: var(--jp-scrollbar-thumb-margin) solid transparent;
  background-clip: content-box;
  border-radius: var(--jp-scrollbar-thumb-radius);
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-hscrollbar::-webkit-scrollbar-track:horizontal {
  border-left: var(--jp-scrollbar-endpad) solid transparent;
  border-right: var(--jp-scrollbar-endpad) solid transparent;
}

[data-jp-theme-scrollbars='true']
  .CodeMirror-vscrollbar::-webkit-scrollbar-track:vertical {
  border-top: var(--jp-scrollbar-endpad) solid transparent;
  border-bottom: var(--jp-scrollbar-endpad) solid transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0px solid transparent;
  border-right: 0px solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0px solid transparent;
  border-bottom: 0px solid transparent;
}

/*
 * Phosphor
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Widget, /* </DEPRECATED> */
.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  cursor: default;
}


/* <DEPRECATED> */ .p-Widget.p-mod-hidden, /* </DEPRECATED> */
.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-CommandPalette, /* </DEPRECATED> */
.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-CommandPalette-search, /* </DEPRECATED> */
.lm-CommandPalette-search {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-content, /* </DEPRECATED> */
.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-CommandPalette-header, /* </DEPRECATED> */
.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}


/* <DEPRECATED> */ .p-CommandPalette-item, /* </DEPRECATED> */
.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}


/* <DEPRECATED> */ .p-CommandPalette-itemIcon, /* </DEPRECATED> */
.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemContent, /* </DEPRECATED> */
.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}


/* <DEPRECATED> */ .p-CommandPalette-itemShortcut, /* </DEPRECATED> */
.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-CommandPalette-itemLabel, /* </DEPRECATED> */
.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
	border:1px solid transparent;
  background-color: transparent;
  position: absolute;
	z-index:1;
	right:3%;
	top: 0;
	bottom: 0;
	margin: auto;
	padding: 7px 0;
	display: none;
	vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
	content: "X";
	display: block;
	width: 15px;
	height: 15px;
	text-align: center;
	color:#000;
	font-weight: normal;
	font-size: 12px;
	cursor: pointer;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-DockPanel, /* </DEPRECATED> */
.lm-DockPanel {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-widget, /* </DEPRECATED> */
.lm-DockPanel-widget {
  z-index: 0;
}


/* <DEPRECATED> */ .p-DockPanel-tabBar, /* </DEPRECATED> */
.lm-DockPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-DockPanel-handle, /* </DEPRECATED> */
.lm-DockPanel-handle {
  z-index: 2;
}


/* <DEPRECATED> */ .p-DockPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-DockPanel-handle:after, /* </DEPRECATED> */
.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='horizontal']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-DockPanel-handle[data-orientation='vertical']:after,
/* </DEPRECATED> */
.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}


/* <DEPRECATED> */ .p-DockPanel-overlay, /* </DEPRECATED> */
.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}


/* <DEPRECATED> */ .p-DockPanel-overlay.p-mod-hidden, /* </DEPRECATED> */
.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-Menu, /* </DEPRECATED> */
.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-Menu-content, /* </DEPRECATED> */
.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}


/* <DEPRECATED> */ .p-Menu-item, /* </DEPRECATED> */
.lm-Menu-item {
  display: table-row;
}


/* <DEPRECATED> */
.p-Menu-item.p-mod-hidden,
.p-Menu-item.p-mod-collapsed,
/* </DEPRECATED> */
.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}


/* <DEPRECATED> */
.p-Menu-itemIcon,
.p-Menu-itemSubmenuIcon,
/* </DEPRECATED> */
.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}


/* <DEPRECATED> */ .p-Menu-itemLabel, /* </DEPRECATED> */
.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}


/* <DEPRECATED> */ .p-Menu-itemShortcut, /* </DEPRECATED> */
.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-MenuBar, /* </DEPRECATED> */
.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-MenuBar-content, /* </DEPRECATED> */
.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}


/* <DEPRECATED> */ .p--MenuBar-item, /* </DEPRECATED> */
.lm-MenuBar-item {
  box-sizing: border-box;
}


/* <DEPRECATED> */
.p-MenuBar-itemIcon,
.p-MenuBar-itemLabel,
/* </DEPRECATED> */
.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-ScrollBar, /* </DEPRECATED> */
.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='horizontal'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-ScrollBar[data-orientation='vertical'],
/* </DEPRECATED> */
.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-ScrollBar-button, /* </DEPRECATED> */
.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-track, /* </DEPRECATED> */
.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}


/* <DEPRECATED> */ .p-ScrollBar-thumb, /* </DEPRECATED> */
.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-SplitPanel-child, /* </DEPRECATED> */
.lm-SplitPanel-child {
  z-index: 0;
}


/* <DEPRECATED> */ .p-SplitPanel-handle, /* </DEPRECATED> */
.lm-SplitPanel-handle {
  z-index: 1;
}


/* <DEPRECATED> */ .p-SplitPanel-handle.p-mod-hidden, /* </DEPRECATED> */
.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-SplitPanel-handle:after, /* </DEPRECATED> */
.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='horizontal'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}


/* <DEPRECATED> */
.p-SplitPanel[data-orientation='vertical'] > .p-SplitPanel-handle:after,
/* </DEPRECATED> */
.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabBar, /* </DEPRECATED> */
.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='horizontal'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar[data-orientation='vertical'], /* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}


/* <DEPRECATED> */ .p-TabBar-content, /* </DEPRECATED> */
.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='horizontal'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}


/* <DEPRECATED> */
.p-TabBar[data-orientation='vertical'] > .p-TabBar-content,
/* </DEPRECATED> */
.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}


/* <DEPRECATED> */ .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
}


/* <DEPRECATED> */
.p-TabBar-tabIcon,
.p-TabBar-tabCloseIcon,
/* </DEPRECATED> */
.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}


/* <DEPRECATED> */ .p-TabBar-tabLabel, /* </DEPRECATED> */
.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}


.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
}


/* <DEPRECATED> */ .p-TabBar-tab.p-mod-hidden, /* </DEPRECATED> */
.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}


.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}


/* <DEPRECATED> */ .p-TabBar.p-mod-dragging .p-TabBar-tab, /* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='horizontal'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging[data-orientation='vertical'] .p-TabBar-tab,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}


/* <DEPRECATED> */
.p-TabBar.p-mod-dragging .p-TabBar-tab.p-mod-dragging,
/* </DEPRECATED> */
.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing : border-box;
  background: inherit;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ .p-TabPanel-tabBar, /* </DEPRECATED> */
.lm-TabPanel-tabBar {
  z-index: 1;
}


/* <DEPRECATED> */ .p-TabPanel-stackedPanel, /* </DEPRECATED> */
.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

@charset "UTF-8";
html{
  -webkit-box-sizing:border-box;
          box-sizing:border-box; }

*,
*::before,
*::after{
  -webkit-box-sizing:inherit;
          box-sizing:inherit; }

body{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none;
  color:#182026;
  font-family:-apple-system, "BlinkMacSystemFont", "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Open Sans", "Helvetica Neue", "Icons16", sans-serif; }

p{
  margin-bottom:10px;
  margin-top:0; }

small{
  font-size:12px; }

strong{
  font-weight:600; }

::-moz-selection{
  background:rgba(125, 188, 255, 0.6); }

::selection{
  background:rgba(125, 188, 255, 0.6); }
.bp3-heading{
  color:#182026;
  font-weight:600;
  margin:0 0 10px;
  padding:0; }
  .bp3-dark .bp3-heading{
    color:#f5f8fa; }

h1.bp3-heading, .bp3-running-text h1{
  font-size:36px;
  line-height:40px; }

h2.bp3-heading, .bp3-running-text h2{
  font-size:28px;
  line-height:32px; }

h3.bp3-heading, .bp3-running-text h3{
  font-size:22px;
  line-height:25px; }

h4.bp3-heading, .bp3-running-text h4{
  font-size:18px;
  line-height:21px; }

h5.bp3-heading, .bp3-running-text h5{
  font-size:16px;
  line-height:19px; }

h6.bp3-heading, .bp3-running-text h6{
  font-size:14px;
  line-height:16px; }
.bp3-ui-text{
  font-size:14px;
  font-weight:400;
  letter-spacing:0;
  line-height:1.28581;
  text-transform:none; }

.bp3-monospace-text{
  font-family:monospace;
  text-transform:none; }

.bp3-text-muted{
  color:#5c7080; }
  .bp3-dark .bp3-text-muted{
    color:#a7b6c2; }

.bp3-text-disabled{
  color:rgba(92, 112, 128, 0.6); }
  .bp3-dark .bp3-text-disabled{
    color:rgba(167, 182, 194, 0.6); }

.bp3-text-overflow-ellipsis{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal; }
.bp3-running-text{
  font-size:14px;
  line-height:1.5; }
  .bp3-running-text h1{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h1{
      color:#f5f8fa; }
  .bp3-running-text h2{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h2{
      color:#f5f8fa; }
  .bp3-running-text h3{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h3{
      color:#f5f8fa; }
  .bp3-running-text h4{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h4{
      color:#f5f8fa; }
  .bp3-running-text h5{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h5{
      color:#f5f8fa; }
  .bp3-running-text h6{
    color:#182026;
    font-weight:600;
    margin-bottom:20px;
    margin-top:40px; }
    .bp3-dark .bp3-running-text h6{
      color:#f5f8fa; }
  .bp3-running-text hr{
    border:none;
    border-bottom:1px solid rgba(16, 22, 26, 0.15);
    margin:20px 0; }
    .bp3-dark .bp3-running-text hr{
      border-color:rgba(255, 255, 255, 0.15); }
  .bp3-running-text p{
    margin:0 0 10px;
    padding:0; }

.bp3-text-large{
  font-size:16px; }

.bp3-text-small{
  font-size:12px; }
a{
  color:#106ba3;
  text-decoration:none; }
  a:hover{
    color:#106ba3;
    cursor:pointer;
    text-decoration:underline; }
  a .bp3-icon, a .bp3-icon-standard, a .bp3-icon-large{
    color:inherit; }
  a code,
  .bp3-dark a code{
    color:inherit; }
  .bp3-dark a,
  .bp3-dark a:hover{
    color:#48aff0; }
    .bp3-dark a .bp3-icon, .bp3-dark a .bp3-icon-standard, .bp3-dark a .bp3-icon-large,
    .bp3-dark a:hover .bp3-icon,
    .bp3-dark a:hover .bp3-icon-standard,
    .bp3-dark a:hover .bp3-icon-large{
      color:inherit; }
.bp3-running-text code, .bp3-code{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  font-size:smaller;
  padding:2px 5px; }
  .bp3-dark .bp3-running-text code, .bp3-running-text .bp3-dark code, .bp3-dark .bp3-code{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
  .bp3-running-text a > code, a > .bp3-code{
    color:#137cbd; }
    .bp3-dark .bp3-running-text a > code, .bp3-running-text .bp3-dark a > code, .bp3-dark a > .bp3-code{
      color:inherit; }

.bp3-running-text pre, .bp3-code-block{
  font-family:monospace;
  text-transform:none;
  background:rgba(255, 255, 255, 0.7);
  border-radius:3px;
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
  color:#182026;
  display:block;
  font-size:13px;
  line-height:1.4;
  margin:10px 0;
  padding:13px 15px 12px;
  word-break:break-all;
  word-wrap:break-word; }
  .bp3-dark .bp3-running-text pre, .bp3-running-text .bp3-dark pre, .bp3-dark .bp3-code-block{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
  .bp3-running-text pre > code, .bp3-code-block > code{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit;
    font-size:inherit;
    padding:0; }

.bp3-running-text kbd, .bp3-key{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#5c7080;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-family:inherit;
  font-size:12px;
  height:24px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  line-height:24px;
  min-width:24px;
  padding:3px 6px;
  vertical-align:middle; }
  .bp3-running-text kbd .bp3-icon, .bp3-key .bp3-icon, .bp3-running-text kbd .bp3-icon-standard, .bp3-key .bp3-icon-standard, .bp3-running-text kbd .bp3-icon-large, .bp3-key .bp3-icon-large{
    margin-right:5px; }
  .bp3-dark .bp3-running-text kbd, .bp3-running-text .bp3-dark kbd, .bp3-dark .bp3-key{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#a7b6c2; }
.bp3-running-text blockquote, .bp3-blockquote{
  border-left:solid 4px rgba(167, 182, 194, 0.5);
  margin:0 0 10px;
  padding:0 20px; }
  .bp3-dark .bp3-running-text blockquote, .bp3-running-text .bp3-dark blockquote, .bp3-dark .bp3-blockquote{
    border-color:rgba(115, 134, 148, 0.5); }
.bp3-running-text ul,
.bp3-running-text ol, .bp3-list{
  margin:10px 0;
  padding-left:30px; }
  .bp3-running-text ul li:not(:last-child), .bp3-running-text ol li:not(:last-child), .bp3-list li:not(:last-child){
    margin-bottom:5px; }
  .bp3-running-text ul ol, .bp3-running-text ol ol, .bp3-list ol,
  .bp3-running-text ul ul,
  .bp3-running-text ol ul,
  .bp3-list ul{
    margin-top:5px; }

.bp3-list-unstyled{
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-list-unstyled li{
    padding:0; }
.bp3-rtl{
  text-align:right; }

.bp3-dark{
  color:#f5f8fa; }

:focus{
  outline:rgba(19, 124, 189, 0.6) auto 2px;
  outline-offset:2px;
  -moz-outline-radius:6px; }

.bp3-focus-disabled :focus{
  outline:none !important; }
  .bp3-focus-disabled :focus ~ .bp3-control-indicator{
    outline:none !important; }

.bp3-alert{
  max-width:400px;
  padding:20px; }

.bp3-alert-body{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-alert-body .bp3-icon{
    font-size:40px;
    margin-right:20px;
    margin-top:0; }

.bp3-alert-contents{
  word-break:break-word; }

.bp3-alert-footer{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:reverse;
      -ms-flex-direction:row-reverse;
          flex-direction:row-reverse;
  margin-top:10px; }
  .bp3-alert-footer .bp3-button{
    margin-left:10px; }
.bp3-breadcrumbs{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  cursor:default;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:wrap;
      flex-wrap:wrap;
  height:30px;
  list-style:none;
  margin:0;
  padding:0; }
  .bp3-breadcrumbs > li{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }
    .bp3-breadcrumbs > li::after{
      background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M10.71 7.29l-4-4a1.003 1.003 0 00-1.42 1.42L8.59 8 5.3 11.29c-.19.18-.3.43-.3.71a1.003 1.003 0 001.71.71l4-4c.18-.18.29-.43.29-.71 0-.28-.11-.53-.29-.71z' fill='%235C7080'/%3e%3c/svg%3e");
      content:"";
      display:block;
      height:16px;
      margin:0 5px;
      width:16px; }
    .bp3-breadcrumbs > li:last-of-type::after{
      display:none; }

.bp3-breadcrumb,
.bp3-breadcrumb-current,
.bp3-breadcrumbs-collapsed{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  font-size:16px; }

.bp3-breadcrumb,
.bp3-breadcrumbs-collapsed{
  color:#5c7080; }

.bp3-breadcrumb:hover{
  text-decoration:none; }

.bp3-breadcrumb.bp3-disabled{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-breadcrumb .bp3-icon{
  margin-right:5px; }

.bp3-breadcrumb-current{
  color:inherit;
  font-weight:600; }
  .bp3-breadcrumb-current .bp3-input{
    font-size:inherit;
    font-weight:inherit;
    vertical-align:baseline; }

.bp3-breadcrumbs-collapsed{
  background:#ced9e0;
  border:none;
  border-radius:3px;
  cursor:pointer;
  margin-right:2px;
  padding:1px 5px;
  vertical-align:text-bottom; }
  .bp3-breadcrumbs-collapsed::before{
    background:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cg fill='%235C7080'%3e%3ccircle cx='2' cy='8.03' r='2'/%3e%3ccircle cx='14' cy='8.03' r='2'/%3e%3ccircle cx='8' cy='8.03' r='2'/%3e%3c/g%3e%3c/svg%3e") center no-repeat;
    content:"";
    display:block;
    height:16px;
    width:16px; }
  .bp3-breadcrumbs-collapsed:hover{
    background:#bfccd6;
    color:#182026;
    text-decoration:none; }

.bp3-dark .bp3-breadcrumb,
.bp3-dark .bp3-breadcrumbs-collapsed{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumbs > li::after{
  color:#a7b6c2; }

.bp3-dark .bp3-breadcrumb.bp3-disabled{
  color:rgba(167, 182, 194, 0.6); }

.bp3-dark .bp3-breadcrumb-current{
  color:#f5f8fa; }

.bp3-dark .bp3-breadcrumbs-collapsed{
  background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-breadcrumbs-collapsed:hover{
    background:rgba(16, 22, 26, 0.6);
    color:#f5f8fa; }
.bp3-button{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  min-height:30px;
  min-width:30px; }
  .bp3-button > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-button > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-button::before,
  .bp3-button > *{
    margin-right:7px; }
  .bp3-button:empty::before,
  .bp3-button > :last-child{
    margin-right:0; }
  .bp3-button:empty{
    padding:0 !important; }
  .bp3-button:disabled, .bp3-button.bp3-disabled{
    cursor:not-allowed; }
  .bp3-button.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button.bp3-align-right,
  .bp3-align-right .bp3-button{
    text-align:right; }
  .bp3-button.bp3-align-left,
  .bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-button:not([class*="bp3-intent-"]){
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026; }
    .bp3-button:not([class*="bp3-intent-"]):hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-button:not([class*="bp3-intent-"]):active, .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active:hover, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active, .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-button.bp3-intent-primary{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover, .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-primary:hover{
      background-color:#106ba3;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:active, .bp3-button.bp3-intent-primary.bp3-active{
      background-color:#0e5a8a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-primary:disabled, .bp3-button.bp3-intent-primary.bp3-disabled{
      background-color:rgba(19, 124, 189, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-success{
    background-color:#0f9960;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-success:hover, .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-success:hover{
      background-color:#0d8050;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:active, .bp3-button.bp3-intent-success.bp3-active{
      background-color:#0a6640;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-success:disabled, .bp3-button.bp3-intent-success.bp3-disabled{
      background-color:rgba(15, 153, 96, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-warning{
    background-color:#d9822b;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover, .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-warning:hover{
      background-color:#bf7326;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:active, .bp3-button.bp3-intent-warning.bp3-active{
      background-color:#a66321;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-warning:disabled, .bp3-button.bp3-intent-warning.bp3-disabled{
      background-color:rgba(217, 130, 43, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button.bp3-intent-danger{
    background-color:#db3737;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover, .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      color:#ffffff; }
    .bp3-button.bp3-intent-danger:hover{
      background-color:#c23030;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:active, .bp3-button.bp3-intent-danger.bp3-active{
      background-color:#a82a2a;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-button.bp3-intent-danger:disabled, .bp3-button.bp3-intent-danger.bp3-disabled{
      background-color:rgba(219, 55, 55, 0.5);
      background-image:none;
      border-color:transparent;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.6); }
  .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
    stroke:#ffffff; }
  .bp3-button.bp3-large,
  .bp3-large .bp3-button{
    min-height:40px;
    min-width:40px;
    font-size:16px;
    padding:5px 15px; }
    .bp3-button.bp3-large::before,
    .bp3-button.bp3-large > *,
    .bp3-large .bp3-button::before,
    .bp3-large .bp3-button > *{
      margin-right:10px; }
    .bp3-button.bp3-large:empty::before,
    .bp3-button.bp3-large > :last-child,
    .bp3-large .bp3-button:empty::before,
    .bp3-large .bp3-button > :last-child{
      margin-right:0; }
  .bp3-button.bp3-small,
  .bp3-small .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-button.bp3-loading{
    position:relative; }
    .bp3-button.bp3-loading[class*="bp3-icon-"]::before{
      visibility:hidden; }
    .bp3-button.bp3-loading .bp3-button-spinner{
      margin:0;
      position:absolute; }
    .bp3-button.bp3-loading > :not(.bp3-button-spinner){
      visibility:hidden; }
  .bp3-button[class*="bp3-icon-"]::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    color:#5c7080; }
  .bp3-button .bp3-icon, .bp3-button .bp3-icon-standard, .bp3-button .bp3-icon-large{
    color:#5c7080; }
    .bp3-button .bp3-icon.bp3-align-right, .bp3-button .bp3-icon-standard.bp3-align-right, .bp3-button .bp3-icon-large.bp3-align-right{
      margin-left:7px; }
  .bp3-button .bp3-icon:first-child:last-child,
  .bp3-button .bp3-spinner + .bp3-icon:last-child{
    margin:0 -7px; }
  .bp3-dark .bp3-button:not([class*="bp3-intent-"]){
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover, .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-button:not([class*="bp3-intent-"]):disabled.bp3-active, .bp3-dark .bp3-button:not([class*="bp3-intent-"]).bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"])[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
    .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-button:not([class*="bp3-intent-"]) .bp3-icon-large{
      color:#a7b6c2; }
  .bp3-dark .bp3-button[class*="bp3-intent-"]{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:hover{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:active, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-active{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-button[class*="bp3-intent-"]:disabled, .bp3-dark .bp3-button[class*="bp3-intent-"].bp3-disabled{
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(255, 255, 255, 0.3); }
    .bp3-dark .bp3-button[class*="bp3-intent-"] .bp3-button-spinner .bp3-spinner-head{
      stroke:#8a9ba8; }
  .bp3-button:disabled::before,
  .bp3-button:disabled .bp3-icon, .bp3-button:disabled .bp3-icon-standard, .bp3-button:disabled .bp3-icon-large, .bp3-button.bp3-disabled::before,
  .bp3-button.bp3-disabled .bp3-icon, .bp3-button.bp3-disabled .bp3-icon-standard, .bp3-button.bp3-disabled .bp3-icon-large, .bp3-button[class*="bp3-intent-"]::before,
  .bp3-button[class*="bp3-intent-"] .bp3-icon, .bp3-button[class*="bp3-intent-"] .bp3-icon-standard, .bp3-button[class*="bp3-intent-"] .bp3-icon-large{
    color:inherit !important; }
  .bp3-button.bp3-minimal{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button.bp3-minimal:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-minimal:active, .bp3-button.bp3-minimal.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-minimal:disabled, .bp3-button.bp3-minimal:disabled:hover, .bp3-button.bp3-minimal.bp3-disabled, .bp3-button.bp3-minimal.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-minimal{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-minimal:hover, .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-minimal:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-minimal:active, .bp3-dark .bp3-button.bp3-minimal.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-minimal:disabled, .bp3-dark .bp3-button.bp3-minimal:disabled:hover, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-minimal:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover, .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover, .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover, .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-minimal.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover, .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-minimal.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-minimal.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button.bp3-outlined{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    border:1px solid rgba(24, 32, 38, 0.2);
    -webkit-box-sizing:border-box;
            box-sizing:border-box; }
    .bp3-button.bp3-outlined:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button.bp3-outlined:active, .bp3-button.bp3-outlined.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button.bp3-outlined{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button.bp3-outlined:hover, .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button.bp3-outlined:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button.bp3-outlined:active, .bp3-dark .bp3-button.bp3-outlined.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button.bp3-outlined:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined:disabled:hover.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover, .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover, .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover, .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover, .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button.bp3-outlined.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
    .bp3-button.bp3-outlined:disabled, .bp3-button.bp3-outlined.bp3-disabled, .bp3-button.bp3-outlined:disabled:hover, .bp3-button.bp3-outlined.bp3-disabled:hover{
      border-color:rgba(92, 112, 128, 0.1); }
    .bp3-dark .bp3-button.bp3-outlined{
      border-color:rgba(255, 255, 255, 0.4); }
      .bp3-dark .bp3-button.bp3-outlined:disabled, .bp3-dark .bp3-button.bp3-outlined:disabled:hover, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-disabled:hover{
        border-color:rgba(255, 255, 255, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-primary{
      border-color:rgba(16, 107, 163, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
        border-color:rgba(16, 107, 163, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary{
        border-color:rgba(72, 175, 240, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-primary.bp3-disabled{
          border-color:rgba(72, 175, 240, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-success{
      border-color:rgba(13, 128, 80, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
        border-color:rgba(13, 128, 80, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success{
        border-color:rgba(61, 204, 145, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-success.bp3-disabled{
          border-color:rgba(61, 204, 145, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-warning{
      border-color:rgba(191, 115, 38, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
        border-color:rgba(191, 115, 38, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning{
        border-color:rgba(255, 179, 102, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-warning.bp3-disabled{
          border-color:rgba(255, 179, 102, 0.2); }
    .bp3-button.bp3-outlined.bp3-intent-danger{
      border-color:rgba(194, 48, 48, 0.6); }
      .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
        border-color:rgba(194, 48, 48, 0.2); }
      .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger{
        border-color:rgba(255, 115, 115, 0.6); }
        .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger:disabled, .bp3-dark .bp3-button.bp3-outlined.bp3-intent-danger.bp3-disabled{
          border-color:rgba(255, 115, 115, 0.2); }

a.bp3-button{
  text-align:center;
  text-decoration:none;
  -webkit-transition:none;
  transition:none; }
  a.bp3-button, a.bp3-button:hover, a.bp3-button:active{
    color:#182026; }
  a.bp3-button.bp3-disabled{
    color:rgba(92, 112, 128, 0.6); }

.bp3-button-text{
  -webkit-box-flex:0;
      -ms-flex:0 1 auto;
          flex:0 1 auto; }

.bp3-button.bp3-align-left .bp3-button-text, .bp3-button.bp3-align-right .bp3-button-text,
.bp3-button-group.bp3-align-left .bp3-button-text,
.bp3-button-group.bp3-align-right .bp3-button-text{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto; }
.bp3-button-group{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex; }
  .bp3-button-group .bp3-button{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    position:relative;
    z-index:4; }
    .bp3-button-group .bp3-button:focus{
      z-index:5; }
    .bp3-button-group .bp3-button:hover{
      z-index:6; }
    .bp3-button-group .bp3-button:active, .bp3-button-group .bp3-button.bp3-active{
      z-index:7; }
    .bp3-button-group .bp3-button:disabled, .bp3-button-group .bp3-button.bp3-disabled{
      z-index:3; }
    .bp3-button-group .bp3-button[class*="bp3-intent-"]{
      z-index:9; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:focus{
        z-index:10; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:hover{
        z-index:11; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:active, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-active{
        z-index:12; }
      .bp3-button-group .bp3-button[class*="bp3-intent-"]:disabled, .bp3-button-group .bp3-button[class*="bp3-intent-"].bp3-disabled{
        z-index:8; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:first-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:first-child){
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    border-bottom-right-radius:0;
    border-top-right-radius:0;
    margin-right:-1px; }
  .bp3-button-group.bp3-minimal .bp3-button{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-button-group.bp3-minimal .bp3-button:hover{
      background:rgba(167, 182, 194, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026;
      text-decoration:none; }
    .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
      background:rgba(115, 134, 148, 0.3);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#182026; }
    .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
      background:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed; }
      .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
        background:rgba(115, 134, 148, 0.3); }
    .bp3-dark .bp3-button-group.bp3-minimal .bp3-button{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:inherit; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:hover{
        background:rgba(138, 155, 168, 0.15); }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-active{
        background:rgba(138, 155, 168, 0.3);
        color:#f5f8fa; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover{
        background:none;
        color:rgba(167, 182, 194, 0.6);
        cursor:not-allowed; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button:disabled:hover.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-disabled:hover.bp3-active{
          background:rgba(138, 155, 168, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
      color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.15);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#106ba3; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(16, 107, 163, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
        stroke:#106ba3; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary{
        color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:hover{
          background:rgba(19, 124, 189, 0.2);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-active{
          background:rgba(19, 124, 189, 0.3);
          color:#48aff0; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled{
          background:none;
          color:rgba(72, 175, 240, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-primary.bp3-disabled.bp3-active{
            background:rgba(19, 124, 189, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
      color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.15);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#0d8050; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(13, 128, 80, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
        stroke:#0d8050; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success{
        color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:hover{
          background:rgba(15, 153, 96, 0.2);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-active{
          background:rgba(15, 153, 96, 0.3);
          color:#3dcc91; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled{
          background:none;
          color:rgba(61, 204, 145, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-success.bp3-disabled.bp3-active{
            background:rgba(15, 153, 96, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
      color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.15);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#bf7326; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(191, 115, 38, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
        stroke:#bf7326; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning{
        color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:hover{
          background:rgba(217, 130, 43, 0.2);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-active{
          background:rgba(217, 130, 43, 0.3);
          color:#ffb366; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled{
          background:none;
          color:rgba(255, 179, 102, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-warning.bp3-disabled.bp3-active{
            background:rgba(217, 130, 43, 0.3); }
    .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
      color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.15);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#c23030; }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(194, 48, 48, 0.5); }
        .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }
      .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
        stroke:#c23030; }
      .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger{
        color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:hover{
          background:rgba(219, 55, 55, 0.2);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-active{
          background:rgba(219, 55, 55, 0.3);
          color:#ff7373; }
        .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled{
          background:none;
          color:rgba(255, 115, 115, 0.5); }
          .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-button-group.bp3-minimal .bp3-button.bp3-intent-danger.bp3-disabled.bp3-active{
            background:rgba(219, 55, 55, 0.3); }
  .bp3-button-group .bp3-popover-wrapper,
  .bp3-button-group .bp3-popover-target{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-button-group .bp3-button.bp3-fill,
  .bp3-button-group.bp3-fill .bp3-button:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-button-group.bp3-vertical{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column;
    vertical-align:top; }
    .bp3-button-group.bp3-vertical.bp3-fill{
      height:100%;
      width:unset; }
    .bp3-button-group.bp3-vertical .bp3-button{
      margin-right:0 !important;
      width:100%; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:first-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:first-child{
      border-radius:3px 3px 0 0; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:last-child .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:last-child{
      border-radius:0 0 3px 3px; }
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
    .bp3-button-group.bp3-vertical:not(.bp3-minimal) > .bp3-button:not(:last-child){
      margin-bottom:-1px; }
  .bp3-button-group.bp3-align-left .bp3-button{
    text-align:left; }
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group:not(.bp3-minimal) > .bp3-button:not(:last-child){
    margin-right:1px; }
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-popover-wrapper:not(:last-child) .bp3-button,
  .bp3-dark .bp3-button-group.bp3-vertical > .bp3-button:not(:last-child){
    margin-bottom:1px; }
.bp3-callout{
  font-size:14px;
  line-height:1.5;
  background-color:rgba(138, 155, 168, 0.15);
  border-radius:3px;
  padding:10px 12px 9px;
  position:relative;
  width:100%; }
  .bp3-callout[class*="bp3-icon-"]{
    padding-left:40px; }
    .bp3-callout[class*="bp3-icon-"]::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout.bp3-callout-icon{
    padding-left:40px; }
    .bp3-callout.bp3-callout-icon > .bp3-icon:first-child{
      color:#5c7080;
      left:10px;
      position:absolute;
      top:10px; }
  .bp3-callout .bp3-heading{
    line-height:20px;
    margin-bottom:5px;
    margin-top:0; }
    .bp3-callout .bp3-heading:last-child{
      margin-bottom:0; }
  .bp3-dark .bp3-callout{
    background-color:rgba(138, 155, 168, 0.2); }
    .bp3-dark .bp3-callout[class*="bp3-icon-"]::before{
      color:#a7b6c2; }
  .bp3-callout.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15); }
    .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-primary .bp3-heading{
      color:#106ba3; }
    .bp3-dark .bp3-callout.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-primary[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-primary > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-primary .bp3-heading{
        color:#48aff0; }
  .bp3-callout.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15); }
    .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-success .bp3-heading{
      color:#0d8050; }
    .bp3-dark .bp3-callout.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-success[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-success > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-success .bp3-heading{
        color:#3dcc91; }
  .bp3-callout.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15); }
    .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-warning .bp3-heading{
      color:#bf7326; }
    .bp3-dark .bp3-callout.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-warning[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-warning > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-warning .bp3-heading{
        color:#ffb366; }
  .bp3-callout.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15); }
    .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
    .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
    .bp3-callout.bp3-intent-danger .bp3-heading{
      color:#c23030; }
    .bp3-dark .bp3-callout.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25); }
      .bp3-dark .bp3-callout.bp3-intent-danger[class*="bp3-icon-"]::before,
      .bp3-dark .bp3-callout.bp3-intent-danger > .bp3-icon:first-child,
      .bp3-dark .bp3-callout.bp3-intent-danger .bp3-heading{
        color:#ff7373; }
  .bp3-running-text .bp3-callout{
    margin:20px 0; }
.bp3-card{
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
  padding:20px;
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-card.bp3-dark,
  .bp3-dark .bp3-card{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-0{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.15), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }
  .bp3-elevation-0.bp3-dark,
  .bp3-dark .bp3-elevation-0{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), 0 0 0 rgba(16, 22, 26, 0), 0 0 0 rgba(16, 22, 26, 0); }

.bp3-elevation-1{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-1.bp3-dark,
  .bp3-dark .bp3-elevation-1{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-elevation-2{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 1px 1px rgba(16, 22, 26, 0.2), 0 2px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-2.bp3-dark,
  .bp3-dark .bp3-elevation-2{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.4), 0 2px 6px rgba(16, 22, 26, 0.4); }

.bp3-elevation-3{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-3.bp3-dark,
  .bp3-dark .bp3-elevation-3{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-elevation-4{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2); }
  .bp3-elevation-4.bp3-dark,
  .bp3-dark .bp3-elevation-4{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:hover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  cursor:pointer; }
  .bp3-card.bp3-interactive:hover.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:hover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }

.bp3-card.bp3-interactive:active{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  opacity:0.9;
  -webkit-transition-duration:0;
          transition-duration:0; }
  .bp3-card.bp3-interactive:active.bp3-dark,
  .bp3-dark .bp3-card.bp3-interactive:active{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-collapse{
  height:0;
  overflow-y:hidden;
  -webkit-transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:height 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-collapse .bp3-collapse-body{
    -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-collapse .bp3-collapse-body[aria-hidden="true"]{
      display:none; }

.bp3-context-menu .bp3-popover-target{
  display:block; }

.bp3-context-menu-popover-target{
  position:fixed; }

.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-dialog-container{
  opacity:1;
  -webkit-transform:scale(1);
          transform:scale(1);
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  min-height:100%;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  width:100%; }
  .bp3-dialog-container.bp3-overlay-enter > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5); }
  .bp3-dialog-container.bp3-overlay-enter-active > .bp3-dialog, .bp3-dialog-container.bp3-overlay-appear-active > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-dialog-container.bp3-overlay-exit > .bp3-dialog{
    opacity:1;
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-dialog-container.bp3-overlay-exit-active > .bp3-dialog{
    opacity:0;
    -webkit-transform:scale(0.5);
            transform:scale(0.5);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-transform;
    transition-property:opacity, -webkit-transform;
    transition-property:opacity, transform;
    transition-property:opacity, transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }

.bp3-dialog{
  background:#ebf1f5;
  border-radius:6px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:30px 0;
  padding-bottom:20px;
  pointer-events:all;
  -webkit-user-select:text;
     -moz-user-select:text;
      -ms-user-select:text;
          user-select:text;
  width:500px; }
  .bp3-dialog:focus{
    outline:0; }
  .bp3-dialog.bp3-dark,
  .bp3-dark .bp3-dialog{
    background:#293742;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-dialog-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background:#ffffff;
  border-radius:6px 6px 0 0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding-left:20px;
  padding-right:5px;
  z-index:30; }
  .bp3-dialog-header .bp3-icon-large,
  .bp3-dialog-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-dialog-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-dialog-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-dialog-header{
    background:#30404d;
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-dialog-header .bp3-icon-large,
    .bp3-dark .bp3-dialog-header .bp3-icon{
      color:#a7b6c2; }

.bp3-dialog-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  margin:20px; }

.bp3-dialog-footer{
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  margin:0 20px; }

.bp3-dialog-footer-actions{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:end;
      -ms-flex-pack:end;
          justify-content:flex-end; }
  .bp3-dialog-footer-actions .bp3-button{
    margin-left:10px; }
.bp3-multistep-dialog-panels{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }

.bp3-multistep-dialog-left-panel{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column; }
  .bp3-dark .bp3-multistep-dialog-left-panel{
    background:#202b33; }

.bp3-multistep-dialog-right-panel{
  background-color:#f5f8fa;
  border-left:1px solid rgba(16, 22, 26, 0.15);
  border-radius:0 0 6px 0;
  -webkit-box-flex:3;
      -ms-flex:3;
          flex:3;
  min-width:0; }
  .bp3-dark .bp3-multistep-dialog-right-panel{
    background-color:#293742;
    border-left:1px solid rgba(16, 22, 26, 0.4); }

.bp3-multistep-dialog-footer{
  background-color:#ffffff;
  border-radius:0 0 6px 0;
  border-top:1px solid rgba(16, 22, 26, 0.15);
  padding:10px; }
  .bp3-dark .bp3-multistep-dialog-footer{
    background:#30404d;
    border-top:1px solid rgba(16, 22, 26, 0.4); }

.bp3-dialog-step-container{
  background-color:#f5f8fa;
  border-bottom:1px solid rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-dialog-step-container{
    background:#293742;
    border-bottom:1px solid rgba(16, 22, 26, 0.4); }
  .bp3-dialog-step-container.bp3-dialog-step-viewed{
    background-color:#ffffff; }
    .bp3-dark .bp3-dialog-step-container.bp3-dialog-step-viewed{
      background:#30404d; }

.bp3-dialog-step{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#f5f8fa;
  border-radius:6px;
  cursor:not-allowed;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:4px;
  padding:6px 14px; }
  .bp3-dark .bp3-dialog-step{
    background:#293742; }
  .bp3-dialog-step-viewed .bp3-dialog-step{
    background-color:#ffffff;
    cursor:pointer; }
    .bp3-dark .bp3-dialog-step-viewed .bp3-dialog-step{
      background:#30404d; }
  .bp3-dialog-step:hover{
    background-color:#f5f8fa; }
    .bp3-dark .bp3-dialog-step:hover{
      background:#293742; }

.bp3-dialog-step-icon{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:rgba(92, 112, 128, 0.6);
  border-radius:50%;
  color:#ffffff;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:25px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  width:25px; }
  .bp3-dark .bp3-dialog-step-icon{
    background-color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#2b95d6; }
  .bp3-dialog-step-viewed .bp3-dialog-step-icon{
    background-color:#8a9ba8; }

.bp3-dialog-step-title{
  color:rgba(92, 112, 128, 0.6);
  -webkit-box-flex:1;
      -ms-flex:1;
          flex:1;
  padding-left:10px; }
  .bp3-dark .bp3-dialog-step-title{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-active.bp3-dialog-step-viewed .bp3-dialog-step-title{
    color:#2b95d6; }
  .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
    color:#182026; }
    .bp3-dark .bp3-dialog-step-viewed:not(.bp3-active) .bp3-dialog-step-title{
      color:#f5f8fa; }
.bp3-drawer{
  background:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0;
  padding:0; }
  .bp3-drawer:focus{
    outline:0; }
  .bp3-drawer.bp3-position-top{
    height:50%;
    left:0;
    right:0;
    top:0; }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter, .bp3-drawer.bp3-position-top.bp3-overlay-appear{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%); }
    .bp3-drawer.bp3-position-top.bp3-overlay-enter-active, .bp3-drawer.bp3-position-top.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-top.bp3-overlay-exit-active{
      -webkit-transform:translateY(-100%);
              transform:translateY(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-bottom{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-enter-active, .bp3-drawer.bp3-position-bottom.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer.bp3-position-bottom.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-left{
    bottom:0;
    left:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter, .bp3-drawer.bp3-position-left.bp3-overlay-appear{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%); }
    .bp3-drawer.bp3-position-left.bp3-overlay-enter-active, .bp3-drawer.bp3-position-left.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-left.bp3-overlay-exit-active{
      -webkit-transform:translateX(-100%);
              transform:translateX(-100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-position-right{
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter, .bp3-drawer.bp3-position-right.bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer.bp3-position-right.bp3-overlay-enter-active, .bp3-drawer.bp3-position-right.bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer.bp3-position-right.bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right):not(.bp3-vertical){
    bottom:0;
    right:0;
    top:0;
    width:50%; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear{
      -webkit-transform:translateX(100%);
              transform:translateX(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-appear-active{
      -webkit-transform:translateX(0);
              transform:translateX(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit{
      -webkit-transform:translateX(0);
              transform:translateX(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right):not(.bp3-vertical).bp3-overlay-exit-active{
      -webkit-transform:translateX(100%);
              transform:translateX(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
  .bp3-position-right).bp3-vertical{
    bottom:0;
    height:50%;
    left:0;
    right:0; }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear{
      -webkit-transform:translateY(100%);
              transform:translateY(100%); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-enter-active, .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-appear-active{
      -webkit-transform:translateY(0);
              transform:translateY(0);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:200ms;
              transition-duration:200ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit{
      -webkit-transform:translateY(0);
              transform:translateY(0); }
    .bp3-drawer:not(.bp3-position-top):not(.bp3-position-bottom):not(.bp3-position-left):not(
    .bp3-position-right).bp3-vertical.bp3-overlay-exit-active{
      -webkit-transform:translateY(100%);
              transform:translateY(100%);
      -webkit-transition-delay:0;
              transition-delay:0;
      -webkit-transition-duration:100ms;
              transition-duration:100ms;
      -webkit-transition-property:-webkit-transform;
      transition-property:-webkit-transform;
      transition-property:transform;
      transition-property:transform, -webkit-transform;
      -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
              transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-drawer.bp3-dark,
  .bp3-dark .bp3-drawer{
    background:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }

.bp3-drawer-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border-radius:0;
  -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:0 1px 0 rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  min-height:40px;
  padding:5px;
  padding-left:20px;
  position:relative; }
  .bp3-drawer-header .bp3-icon-large,
  .bp3-drawer-header .bp3-icon{
    color:#5c7080;
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    margin-right:10px; }
  .bp3-drawer-header .bp3-heading{
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:inherit;
    margin:0; }
    .bp3-drawer-header .bp3-heading:last-child{
      margin-right:20px; }
  .bp3-dark .bp3-drawer-header{
    -webkit-box-shadow:0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:0 1px 0 rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-drawer-header .bp3-icon-large,
    .bp3-dark .bp3-drawer-header .bp3-icon{
      color:#a7b6c2; }

.bp3-drawer-body{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  line-height:18px;
  overflow:auto; }

.bp3-drawer-footer{
  -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  padding:10px 20px;
  position:relative; }
  .bp3-dark .bp3-drawer-footer{
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.4); }
.bp3-editable-text{
  cursor:text;
  display:inline-block;
  max-width:100%;
  position:relative;
  vertical-align:top;
  white-space:nowrap; }
  .bp3-editable-text::before{
    bottom:-3px;
    left:-3px;
    position:absolute;
    right:-3px;
    top:-3px;
    border-radius:3px;
    content:"";
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9), box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#137cbd; }
  .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(19, 124, 189, 0.4); }
  .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#0f9960; }
  .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px rgba(15, 153, 96, 0.4); }
  .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#d9822b; }
  .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px rgba(217, 130, 43, 0.4); }
  .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-input,
  .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#db3737; }
  .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px rgba(219, 55, 55, 0.4); }
  .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-editable-text:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(255, 255, 255, 0.15); }
  .bp3-dark .bp3-editable-text.bp3-editable-text-editing::before{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-disabled::before{
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary .bp3-editable-text-content{
    color:#48aff0; }
  .bp3-dark .bp3-editable-text.bp3-intent-primary:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4);
            box-shadow:0 0 0 0 rgba(72, 175, 240, 0), 0 0 0 0 rgba(72, 175, 240, 0), inset 0 0 0 1px rgba(72, 175, 240, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-primary.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #48aff0, 0 0 0 3px rgba(72, 175, 240, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success .bp3-editable-text-content{
    color:#3dcc91; }
  .bp3-dark .bp3-editable-text.bp3-intent-success:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4);
            box-shadow:0 0 0 0 rgba(61, 204, 145, 0), 0 0 0 0 rgba(61, 204, 145, 0), inset 0 0 0 1px rgba(61, 204, 145, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-success.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #3dcc91, 0 0 0 3px rgba(61, 204, 145, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning .bp3-editable-text-content{
    color:#ffb366; }
  .bp3-dark .bp3-editable-text.bp3-intent-warning:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4);
            box-shadow:0 0 0 0 rgba(255, 179, 102, 0), 0 0 0 0 rgba(255, 179, 102, 0), inset 0 0 0 1px rgba(255, 179, 102, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-warning.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ffb366, 0 0 0 3px rgba(255, 179, 102, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger .bp3-editable-text-content{
    color:#ff7373; }
  .bp3-dark .bp3-editable-text.bp3-intent-danger:hover::before{
    -webkit-box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4);
            box-shadow:0 0 0 0 rgba(255, 115, 115, 0), 0 0 0 0 rgba(255, 115, 115, 0), inset 0 0 0 1px rgba(255, 115, 115, 0.4); }
  .bp3-dark .bp3-editable-text.bp3-intent-danger.bp3-editable-text-editing::before{
    -webkit-box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #ff7373, 0 0 0 3px rgba(255, 115, 115, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-editable-text-input,
.bp3-editable-text-content{
  color:inherit;
  display:inherit;
  font:inherit;
  letter-spacing:inherit;
  max-width:inherit;
  min-width:inherit;
  position:relative;
  resize:none;
  text-transform:inherit;
  vertical-align:top; }

.bp3-editable-text-input{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0;
  white-space:pre-wrap;
  width:100%; }
  .bp3-editable-text-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-editable-text-input:focus{
    outline:none; }
  .bp3-editable-text-input::-ms-clear{
    display:none; }

.bp3-editable-text-content{
  overflow:hidden;
  padding-right:2px;
  text-overflow:ellipsis;
  white-space:pre; }
  .bp3-editable-text-editing > .bp3-editable-text-content{
    left:0;
    position:absolute;
    visibility:hidden; }
  .bp3-editable-text-placeholder > .bp3-editable-text-content{
    color:rgba(92, 112, 128, 0.6); }
    .bp3-dark .bp3-editable-text-placeholder > .bp3-editable-text-content{
      color:rgba(167, 182, 194, 0.6); }

.bp3-editable-text.bp3-multiline{
  display:block; }
  .bp3-editable-text.bp3-multiline .bp3-editable-text-content{
    overflow:auto;
    white-space:pre-wrap;
    word-wrap:break-word; }
.bp3-divider{
  border-bottom:1px solid rgba(16, 22, 26, 0.15);
  border-right:1px solid rgba(16, 22, 26, 0.15);
  margin:5px; }
  .bp3-dark .bp3-divider{
    border-color:rgba(16, 22, 26, 0.4); }
.bp3-control-group{
  -webkit-transform:translateZ(0);
          transform:translateZ(0);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:stretch;
      -ms-flex-align:stretch;
          align-items:stretch; }
  .bp3-control-group > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select,
  .bp3-control-group .bp3-input,
  .bp3-control-group .bp3-select{
    position:relative; }
  .bp3-control-group .bp3-input{
    border-radius:inherit;
    z-index:2; }
    .bp3-control-group .bp3-input:focus{
      border-radius:3px;
      z-index:14; }
    .bp3-control-group .bp3-input[class*="bp3-intent"]{
      z-index:13; }
      .bp3-control-group .bp3-input[class*="bp3-intent"]:focus{
        z-index:15; }
    .bp3-control-group .bp3-input[readonly], .bp3-control-group .bp3-input:disabled, .bp3-control-group .bp3-input.bp3-disabled{
      z-index:1; }
  .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input{
    z-index:13; }
    .bp3-control-group .bp3-input-group[class*="bp3-intent"] .bp3-input:focus{
      z-index:15; }
  .bp3-control-group .bp3-button,
  .bp3-control-group .bp3-html-select select,
  .bp3-control-group .bp3-select select{
    -webkit-transform:translateZ(0);
            transform:translateZ(0);
    border-radius:inherit;
    z-index:4; }
    .bp3-control-group .bp3-button:focus,
    .bp3-control-group .bp3-html-select select:focus,
    .bp3-control-group .bp3-select select:focus{
      z-index:5; }
    .bp3-control-group .bp3-button:hover,
    .bp3-control-group .bp3-html-select select:hover,
    .bp3-control-group .bp3-select select:hover{
      z-index:6; }
    .bp3-control-group .bp3-button:active,
    .bp3-control-group .bp3-html-select select:active,
    .bp3-control-group .bp3-select select:active{
      z-index:7; }
    .bp3-control-group .bp3-button[readonly], .bp3-control-group .bp3-button:disabled, .bp3-control-group .bp3-button.bp3-disabled,
    .bp3-control-group .bp3-html-select select[readonly],
    .bp3-control-group .bp3-html-select select:disabled,
    .bp3-control-group .bp3-html-select select.bp3-disabled,
    .bp3-control-group .bp3-select select[readonly],
    .bp3-control-group .bp3-select select:disabled,
    .bp3-control-group .bp3-select select.bp3-disabled{
      z-index:3; }
    .bp3-control-group .bp3-button[class*="bp3-intent"],
    .bp3-control-group .bp3-html-select select[class*="bp3-intent"],
    .bp3-control-group .bp3-select select[class*="bp3-intent"]{
      z-index:9; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:focus,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:focus{
        z-index:10; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:hover,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:hover{
        z-index:11; }
      .bp3-control-group .bp3-button[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:active,
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:active{
        z-index:12; }
      .bp3-control-group .bp3-button[class*="bp3-intent"][readonly], .bp3-control-group .bp3-button[class*="bp3-intent"]:disabled, .bp3-control-group .bp3-button[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-html-select select[class*="bp3-intent"].bp3-disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"][readonly],
      .bp3-control-group .bp3-select select[class*="bp3-intent"]:disabled,
      .bp3-control-group .bp3-select select[class*="bp3-intent"].bp3-disabled{
        z-index:8; }
  .bp3-control-group .bp3-input-group > .bp3-icon,
  .bp3-control-group .bp3-input-group > .bp3-button,
  .bp3-control-group .bp3-input-group > .bp3-input-left-container,
  .bp3-control-group .bp3-input-group > .bp3-input-action{
    z-index:16; }
  .bp3-control-group .bp3-select::after,
  .bp3-control-group .bp3-html-select::after,
  .bp3-control-group .bp3-select > .bp3-icon,
  .bp3-control-group .bp3-html-select > .bp3-icon{
    z-index:17; }
  .bp3-control-group .bp3-select:focus-within{
    z-index:5; }
  .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:-1px; }
  .bp3-control-group:not(.bp3-vertical) > .bp3-divider:not(:first-child){
    margin-left:6px; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > *:not(.bp3-divider){
    margin-right:0; }
  .bp3-dark .bp3-control-group:not(.bp3-vertical) > .bp3-button + .bp3-button{
    margin-left:1px; }
  .bp3-control-group .bp3-popover-wrapper,
  .bp3-control-group .bp3-popover-target{
    border-radius:inherit; }
  .bp3-control-group > :first-child{
    border-radius:3px 0 0 3px; }
  .bp3-control-group > :last-child{
    border-radius:0 3px 3px 0;
    margin-right:0; }
  .bp3-control-group > :only-child{
    border-radius:3px;
    margin-right:0; }
  .bp3-control-group .bp3-input-group .bp3-button{
    border-radius:3px; }
  .bp3-control-group .bp3-numeric-input:not(:first-child) .bp3-input-group{
    border-bottom-left-radius:0;
    border-top-left-radius:0; }
  .bp3-control-group.bp3-fill{
    width:100%; }
  .bp3-control-group > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-fill > *:not(.bp3-fixed){
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto; }
  .bp3-control-group.bp3-vertical{
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-control-group.bp3-vertical > *{
      margin-top:-1px; }
    .bp3-control-group.bp3-vertical > :first-child{
      border-radius:3px 3px 0 0;
      margin-top:0; }
    .bp3-control-group.bp3-vertical > :last-child{
      border-radius:0 0 3px 3px; }
.bp3-control{
  cursor:pointer;
  display:block;
  margin-bottom:10px;
  position:relative;
  text-transform:none; }
  .bp3-control input:checked ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control input:checked ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control:hover input:checked ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control input:not(:disabled):active:checked ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control input:disabled:checked ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control:not(.bp3-align-right){
    padding-left:26px; }
    .bp3-control:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-26px; }
  .bp3-control.bp3-align-right{
    padding-right:26px; }
    .bp3-control.bp3-align-right .bp3-control-indicator{
      margin-right:-26px; }
  .bp3-control.bp3-disabled{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-control.bp3-inline{
    display:inline-block;
    margin-right:20px; }
  .bp3-control input{
    left:0;
    opacity:0;
    position:absolute;
    top:0;
    z-index:-1; }
  .bp3-control .bp3-control-indicator{
    background-clip:padding-box;
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    border:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    cursor:pointer;
    display:inline-block;
    font-size:16px;
    height:1em;
    margin-right:10px;
    margin-top:-3px;
    position:relative;
    -webkit-user-select:none;
       -moz-user-select:none;
        -ms-user-select:none;
            user-select:none;
    vertical-align:middle;
    width:1em; }
    .bp3-control .bp3-control-indicator::before{
      content:"";
      display:block;
      height:1em;
      width:1em; }
  .bp3-control:hover .bp3-control-indicator{
    background-color:#ebf1f5; }
  .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
    background:#d8e1e8;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    cursor:not-allowed; }
  .bp3-control input:focus ~ .bp3-control-indicator{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:2px;
    -moz-outline-radius:6px; }
  .bp3-control.bp3-align-right .bp3-control-indicator{
    float:right;
    margin-left:10px;
    margin-top:1px; }
  .bp3-control.bp3-large{
    font-size:16px; }
    .bp3-control.bp3-large:not(.bp3-align-right){
      padding-left:30px; }
      .bp3-control.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
        margin-left:-30px; }
    .bp3-control.bp3-large.bp3-align-right{
      padding-right:30px; }
      .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
        margin-right:-30px; }
    .bp3-control.bp3-large .bp3-control-indicator{
      font-size:20px; }
    .bp3-control.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-top:0; }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    background-color:#137cbd;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.1)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.1), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
    color:#ffffff; }
  .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 -1px 0 rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background:#0e5a8a;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-dark .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox:hover input:indeterminate ~ .bp3-control-indicator{
    background-color:#106ba3;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-checkbox input:not(:disabled):active:indeterminate ~ .bp3-control-indicator{
    background-color:#0e5a8a;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-control.bp3-checkbox .bp3-control-indicator{
    border-radius:3px; }
  .bp3-control.bp3-checkbox input:checked ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M12 5c-.28 0-.53.11-.71.29L7 9.59l-2.29-2.3a1.003 1.003 0 00-1.42 1.42l3 3c.18.18.43.29.71.29s.53-.11.71-.29l5-5A1.003 1.003 0 0012 5z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-checkbox input:indeterminate ~ .bp3-control-indicator::before{
    background-image:url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M11 7H5c-.55 0-1 .45-1 1s.45 1 1 1h6c.55 0 1-.45 1-1s-.45-1-1-1z' fill='white'/%3e%3c/svg%3e"); }
  .bp3-control.bp3-radio .bp3-control-indicator{
    border-radius:50%; }
  .bp3-control.bp3-radio input:checked ~ .bp3-control-indicator::before{
    background-image:radial-gradient(#ffffff, #ffffff 28%, transparent 32%); }
  .bp3-control.bp3-radio input:checked:disabled ~ .bp3-control-indicator::before{
    opacity:0.5; }
  .bp3-control.bp3-radio input:focus ~ .bp3-control-indicator{
    -moz-outline-radius:16px; }
  .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(167, 182, 194, 0.5); }
  .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(115, 134, 148, 0.5); }
  .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(92, 112, 128, 0.5); }
  .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(206, 217, 224, 0.5); }
    .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(19, 124, 189, 0.5); }
    .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(255, 255, 255, 0.8); }
  .bp3-control.bp3-switch:not(.bp3-align-right){
    padding-left:38px; }
    .bp3-control.bp3-switch:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-38px; }
  .bp3-control.bp3-switch.bp3-align-right{
    padding-right:38px; }
    .bp3-control.bp3-switch.bp3-align-right .bp3-control-indicator{
      margin-right:-38px; }
  .bp3-control.bp3-switch .bp3-control-indicator{
    border:none;
    border-radius:1.75em;
    -webkit-box-shadow:none !important;
            box-shadow:none !important;
    min-width:1.75em;
    -webkit-transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:background-color 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:auto; }
    .bp3-control.bp3-switch .bp3-control-indicator::before{
      background:#ffffff;
      border-radius:50%;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
      height:calc(1em - 4px);
      left:0;
      margin:2px;
      position:absolute;
      -webkit-transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      transition:left 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
      width:calc(1em - 4px); }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    left:calc(100% - 1em); }
  .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right){
    padding-left:45px; }
    .bp3-control.bp3-switch.bp3-large:not(.bp3-align-right) .bp3-control-indicator{
      margin-left:-45px; }
  .bp3-control.bp3-switch.bp3-large.bp3-align-right{
    padding-right:45px; }
    .bp3-control.bp3-switch.bp3-large.bp3-align-right .bp3-control-indicator{
      margin-right:-45px; }
  .bp3-dark .bp3-control.bp3-switch input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-control.bp3-switch:hover input ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.7); }
  .bp3-dark .bp3-control.bp3-switch input:not(:disabled):active ~ .bp3-control-indicator{
    background:rgba(16, 22, 26, 0.9); }
  .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator{
    background:rgba(57, 75, 89, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator{
    background:#137cbd; }
  .bp3-dark .bp3-control.bp3-switch:hover input:checked ~ .bp3-control-indicator{
    background:#106ba3; }
  .bp3-dark .bp3-control.bp3-switch input:checked:not(:disabled):active ~ .bp3-control-indicator{
    background:#0e5a8a; }
  .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator{
    background:rgba(14, 90, 138, 0.5); }
    .bp3-dark .bp3-control.bp3-switch input:checked:disabled ~ .bp3-control-indicator::before{
      background:rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch .bp3-control-indicator::before{
    background:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator::before{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-control.bp3-switch .bp3-switch-inner-text{
    font-size:0.7em;
    text-align:center; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:first-child{
    line-height:0;
    margin-left:0.5em;
    margin-right:1.2em;
    visibility:hidden; }
  .bp3-control.bp3-switch .bp3-control-indicator-child:last-child{
    line-height:1em;
    margin-left:1.2em;
    margin-right:0.5em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:first-child{
    line-height:1em;
    visibility:visible; }
  .bp3-control.bp3-switch input:checked ~ .bp3-control-indicator .bp3-control-indicator-child:last-child{
    line-height:0;
    visibility:hidden; }
  .bp3-dark .bp3-control{
    color:#f5f8fa; }
    .bp3-dark .bp3-control.bp3-disabled{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-control .bp3-control-indicator{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-control:hover .bp3-control-indicator{
      background-color:#30404d; }
    .bp3-dark .bp3-control input:not(:disabled):active ~ .bp3-control-indicator{
      background:#202b33;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-control input:disabled ~ .bp3-control-indicator{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      cursor:not-allowed; }
    .bp3-dark .bp3-control.bp3-checkbox input:disabled:checked ~ .bp3-control-indicator, .bp3-dark .bp3-control.bp3-checkbox input:disabled:indeterminate ~ .bp3-control-indicator{
      color:rgba(167, 182, 194, 0.6); }
.bp3-file-input{
  cursor:pointer;
  display:inline-block;
  height:30px;
  position:relative; }
  .bp3-file-input input{
    margin:0;
    min-width:200px;
    opacity:0; }
    .bp3-file-input input:disabled + .bp3-file-upload-input,
    .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
      background:rgba(206, 217, 224, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      resize:none; }
      .bp3-file-input input:disabled + .bp3-file-upload-input::after,
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
        background-color:rgba(206, 217, 224, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(92, 112, 128, 0.6);
        cursor:not-allowed;
        outline:none; }
        .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active:hover,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active,
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active:hover{
          background:rgba(206, 217, 224, 0.7); }
      .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input, .bp3-dark
      .bp3-file-input input.bp3-disabled + .bp3-file-upload-input{
        background:rgba(57, 75, 89, 0.5);
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after, .bp3-dark
        .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after{
          background-color:rgba(57, 75, 89, 0.5);
          background-image:none;
          -webkit-box-shadow:none;
                  box-shadow:none;
          color:rgba(167, 182, 194, 0.6); }
          .bp3-dark .bp3-file-input input:disabled + .bp3-file-upload-input::after.bp3-active, .bp3-dark
          .bp3-file-input input.bp3-disabled + .bp3-file-upload-input::after.bp3-active{
            background:rgba(57, 75, 89, 0.7); }
  .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#182026; }
  .bp3-dark .bp3-file-input.bp3-file-input-has-selection .bp3-file-upload-input{
    color:#f5f8fa; }
  .bp3-file-input.bp3-fill{
    width:100%; }
  .bp3-file-input.bp3-large,
  .bp3-large .bp3-file-input{
    height:40px; }
  .bp3-file-input .bp3-file-upload-input-custom-text::after{
    content:attr(bp3-button-text); }

.bp3-file-upload-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle;
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:rgba(92, 112, 128, 0.6);
  left:0;
  padding-right:80px;
  position:absolute;
  right:0;
  top:0;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-file-upload-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-file-upload-input:focus, .bp3-file-upload-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-file-upload-input[type="search"], .bp3-file-upload-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-file-upload-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-file-upload-input:disabled, .bp3-file-upload-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-file-upload-input::after{
    background-color:#f5f8fa;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    color:#182026;
    min-height:24px;
    min-width:24px;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    border-radius:3px;
    content:"Browse";
    line-height:24px;
    margin:3px;
    position:absolute;
    right:0;
    text-align:center;
    top:0;
    width:70px; }
    .bp3-file-upload-input::after:hover{
      background-clip:padding-box;
      background-color:#ebf1f5;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
    .bp3-file-upload-input::after:active, .bp3-file-upload-input::after.bp3-active{
      background-color:#d8e1e8;
      background-image:none;
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-file-upload-input::after:disabled, .bp3-file-upload-input::after.bp3-disabled{
      background-color:rgba(206, 217, 224, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(92, 112, 128, 0.6);
      cursor:not-allowed;
      outline:none; }
      .bp3-file-upload-input::after:disabled.bp3-active, .bp3-file-upload-input::after:disabled.bp3-active:hover, .bp3-file-upload-input::after.bp3-disabled.bp3-active, .bp3-file-upload-input::after.bp3-disabled.bp3-active:hover{
        background:rgba(206, 217, 224, 0.7); }
  .bp3-file-upload-input:hover::after{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-file-upload-input:active::after{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-large .bp3-file-upload-input{
    font-size:16px;
    height:40px;
    line-height:40px;
    padding-right:95px; }
    .bp3-large .bp3-file-upload-input[type="search"], .bp3-large .bp3-file-upload-input.bp3-round{
      padding:0 15px; }
    .bp3-large .bp3-file-upload-input::after{
      min-height:30px;
      min-width:30px;
      line-height:30px;
      margin:5px;
      width:85px; }
  .bp3-dark .bp3-file-upload-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:disabled, .bp3-dark .bp3-file-upload-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-file-upload-input::after{
      background-color:#394b59;
      background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
      background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
      color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover, .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        color:#f5f8fa; }
      .bp3-dark .bp3-file-upload-input::after:hover{
        background-color:#30404d;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-file-upload-input::after:active, .bp3-dark .bp3-file-upload-input::after.bp3-active{
        background-color:#202b33;
        background-image:none;
        -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
                box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
      .bp3-dark .bp3-file-upload-input::after:disabled, .bp3-dark .bp3-file-upload-input::after.bp3-disabled{
        background-color:rgba(57, 75, 89, 0.5);
        background-image:none;
        -webkit-box-shadow:none;
                box-shadow:none;
        color:rgba(167, 182, 194, 0.6); }
        .bp3-dark .bp3-file-upload-input::after:disabled.bp3-active, .bp3-dark .bp3-file-upload-input::after.bp3-disabled.bp3-active{
          background:rgba(57, 75, 89, 0.7); }
      .bp3-dark .bp3-file-upload-input::after .bp3-button-spinner .bp3-spinner-head{
        background:rgba(16, 22, 26, 0.5);
        stroke:#8a9ba8; }
    .bp3-dark .bp3-file-upload-input:hover::after{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-file-upload-input:active::after{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
.bp3-file-upload-input::after{
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
.bp3-form-group{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin:0 0 15px; }
  .bp3-form-group label.bp3-label{
    margin-bottom:5px; }
  .bp3-form-group .bp3-control{
    margin-top:7px; }
  .bp3-form-group .bp3-form-helper-text{
    color:#5c7080;
    font-size:12px;
    margin-top:5px; }
  .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#106ba3; }
  .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#0d8050; }
  .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#bf7326; }
  .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#c23030; }
  .bp3-form-group.bp3-inline{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row; }
    .bp3-form-group.bp3-inline.bp3-large label.bp3-label{
      line-height:40px;
      margin:0 10px 0 0; }
    .bp3-form-group.bp3-inline label.bp3-label{
      line-height:30px;
      margin:0 10px 0 0; }
  .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-dark .bp3-form-group.bp3-intent-primary .bp3-form-helper-text{
    color:#48aff0; }
  .bp3-dark .bp3-form-group.bp3-intent-success .bp3-form-helper-text{
    color:#3dcc91; }
  .bp3-dark .bp3-form-group.bp3-intent-warning .bp3-form-helper-text{
    color:#ffb366; }
  .bp3-dark .bp3-form-group.bp3-intent-danger .bp3-form-helper-text{
    color:#ff7373; }
  .bp3-dark .bp3-form-group .bp3-form-helper-text{
    color:#a7b6c2; }
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-label,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-text-muted,
  .bp3-dark .bp3-form-group.bp3-disabled .bp3-form-helper-text{
    color:rgba(167, 182, 194, 0.6) !important; }
.bp3-input-group{
  display:block;
  position:relative; }
  .bp3-input-group .bp3-input{
    position:relative;
    width:100%; }
    .bp3-input-group .bp3-input:not(:first-child){
      padding-left:30px; }
    .bp3-input-group .bp3-input:not(:last-child){
      padding-right:30px; }
  .bp3-input-group .bp3-input-action,
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-button,
  .bp3-input-group > .bp3-icon{
    position:absolute;
    top:0; }
    .bp3-input-group .bp3-input-action:first-child,
    .bp3-input-group > .bp3-input-left-container:first-child,
    .bp3-input-group > .bp3-button:first-child,
    .bp3-input-group > .bp3-icon:first-child{
      left:0; }
    .bp3-input-group .bp3-input-action:last-child,
    .bp3-input-group > .bp3-input-left-container:last-child,
    .bp3-input-group > .bp3-button:last-child,
    .bp3-input-group > .bp3-icon:last-child{
      right:0; }
  .bp3-input-group .bp3-button{
    min-height:24px;
    min-width:24px;
    margin:3px;
    padding:0 7px; }
    .bp3-input-group .bp3-button:empty{
      padding:0; }
  .bp3-input-group > .bp3-input-left-container,
  .bp3-input-group > .bp3-icon{
    z-index:1; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon{
    color:#5c7080; }
    .bp3-input-group > .bp3-input-left-container > .bp3-icon:empty,
    .bp3-input-group > .bp3-icon:empty{
      font-family:"Icons16", sans-serif;
      font-size:16px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased; }
  .bp3-input-group > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group > .bp3-icon,
  .bp3-input-group .bp3-input-action > .bp3-spinner{
    margin:7px; }
  .bp3-input-group .bp3-tag{
    margin:5px; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus),
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
    color:#5c7080; }
    .bp3-dark .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus), .bp3-dark
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus){
      color:#a7b6c2; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:not(:hover):not(:focus) .bp3-icon-large{
      color:#5c7080; }
  .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled,
  .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled{
    color:rgba(92, 112, 128, 0.6) !important; }
    .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-standard, .bp3-input-group .bp3-input:not(:focus) + .bp3-button.bp3-minimal:disabled .bp3-icon-large,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-standard,
    .bp3-input-group .bp3-input:not(:focus) + .bp3-input-action .bp3-button.bp3-minimal:disabled .bp3-icon-large{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-input-group.bp3-disabled{
    cursor:not-allowed; }
    .bp3-input-group.bp3-disabled .bp3-icon{
      color:rgba(92, 112, 128, 0.6); }
  .bp3-input-group.bp3-large .bp3-button{
    min-height:30px;
    min-width:30px;
    margin:5px; }
  .bp3-input-group.bp3-large > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-large > .bp3-icon,
  .bp3-input-group.bp3-large .bp3-input-action > .bp3-spinner{
    margin:12px; }
  .bp3-input-group.bp3-large .bp3-input{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input-group.bp3-large .bp3-input[type="search"], .bp3-input-group.bp3-large .bp3-input.bp3-round{
      padding:0 15px; }
    .bp3-input-group.bp3-large .bp3-input:not(:first-child){
      padding-left:40px; }
    .bp3-input-group.bp3-large .bp3-input:not(:last-child){
      padding-right:40px; }
  .bp3-input-group.bp3-small .bp3-button{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small .bp3-tag{
    min-height:20px;
    min-width:20px;
    margin:2px; }
  .bp3-input-group.bp3-small > .bp3-input-left-container > .bp3-icon,
  .bp3-input-group.bp3-small > .bp3-icon,
  .bp3-input-group.bp3-small .bp3-input-action > .bp3-spinner{
    margin:4px; }
  .bp3-input-group.bp3-small .bp3-input{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input-group.bp3-small .bp3-input[type="search"], .bp3-input-group.bp3-small .bp3-input.bp3-round{
      padding:0 12px; }
    .bp3-input-group.bp3-small .bp3-input:not(:first-child){
      padding-left:24px; }
    .bp3-input-group.bp3-small .bp3-input:not(:last-child){
      padding-right:24px; }
  .bp3-input-group.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-input-group.bp3-round .bp3-button,
  .bp3-input-group.bp3-round .bp3-input,
  .bp3-input-group.bp3-round .bp3-tag{
    border-radius:30px; }
  .bp3-dark .bp3-input-group .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-input-group.bp3-disabled .bp3-icon{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-input-group.bp3-intent-primary .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-primary .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input-group.bp3-intent-primary .bp3-input:disabled, .bp3-input-group.bp3-intent-primary .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-primary > .bp3-icon{
    color:#106ba3; }
    .bp3-dark .bp3-input-group.bp3-intent-primary > .bp3-icon{
      color:#48aff0; }
  .bp3-input-group.bp3-intent-success .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-success .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input-group.bp3-intent-success .bp3-input:disabled, .bp3-input-group.bp3-intent-success .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-success > .bp3-icon{
    color:#0d8050; }
    .bp3-dark .bp3-input-group.bp3-intent-success > .bp3-icon{
      color:#3dcc91; }
  .bp3-input-group.bp3-intent-warning .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-warning .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input-group.bp3-intent-warning .bp3-input:disabled, .bp3-input-group.bp3-intent-warning .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-warning > .bp3-icon{
    color:#bf7326; }
    .bp3-dark .bp3-input-group.bp3-intent-warning > .bp3-icon{
      color:#ffb366; }
  .bp3-input-group.bp3-intent-danger .bp3-input{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input-group.bp3-intent-danger .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input-group.bp3-intent-danger .bp3-input:disabled, .bp3-input-group.bp3-intent-danger .bp3-input.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-input-group.bp3-intent-danger > .bp3-icon{
    color:#c23030; }
    .bp3-dark .bp3-input-group.bp3-intent-danger > .bp3-icon{
      color:#ff7373; }
.bp3-input{
  -webkit-appearance:none;
     -moz-appearance:none;
          appearance:none;
  background:#ffffff;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
  color:#182026;
  font-size:14px;
  font-weight:400;
  height:30px;
  line-height:30px;
  outline:none;
  padding:0 10px;
  -webkit-transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-box-shadow 100ms cubic-bezier(0.4, 1, 0.75, 0.9);
  vertical-align:middle; }
  .bp3-input::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input:focus, .bp3-input.bp3-active{
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-input[type="search"], .bp3-input.bp3-round{
    border-radius:30px;
    -webkit-box-sizing:border-box;
            box-sizing:border-box;
    padding-left:10px; }
  .bp3-input[readonly]{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.15); }
  .bp3-input:disabled, .bp3-input.bp3-disabled{
    background:rgba(206, 217, 224, 0.5);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    resize:none; }
  .bp3-input.bp3-large{
    font-size:16px;
    height:40px;
    line-height:40px; }
    .bp3-input.bp3-large[type="search"], .bp3-input.bp3-large.bp3-round{
      padding:0 15px; }
  .bp3-input.bp3-small{
    font-size:12px;
    height:24px;
    line-height:24px;
    padding-left:8px;
    padding-right:8px; }
    .bp3-input.bp3-small[type="search"], .bp3-input.bp3-small.bp3-round{
      padding:0 12px; }
  .bp3-input.bp3-fill{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    width:100%; }
  .bp3-dark .bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-input:disabled, .bp3-dark .bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-input.bp3-intent-primary{
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-primary[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #137cbd;
              box-shadow:inset 0 0 0 1px #137cbd; }
    .bp3-input.bp3-intent-primary:disabled, .bp3-input.bp3-intent-primary.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px #137cbd, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary:focus{
        -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-primary[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #137cbd;
                box-shadow:inset 0 0 0 1px #137cbd; }
      .bp3-dark .bp3-input.bp3-intent-primary:disabled, .bp3-dark .bp3-input.bp3-intent-primary.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-success{
    -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success:focus{
      -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-success[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #0f9960;
              box-shadow:inset 0 0 0 1px #0f9960; }
    .bp3-input.bp3-intent-success:disabled, .bp3-input.bp3-intent-success.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-success{
      -webkit-box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), 0 0 0 0 rgba(15, 153, 96, 0), inset 0 0 0 1px #0f9960, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success:focus{
        -webkit-box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #0f9960, 0 0 0 1px #0f9960, 0 0 0 3px rgba(15, 153, 96, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-success[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #0f9960;
                box-shadow:inset 0 0 0 1px #0f9960; }
      .bp3-dark .bp3-input.bp3-intent-success:disabled, .bp3-dark .bp3-input.bp3-intent-success.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-warning{
    -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning:focus{
      -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-warning[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #d9822b;
              box-shadow:inset 0 0 0 1px #d9822b; }
    .bp3-input.bp3-intent-warning:disabled, .bp3-input.bp3-intent-warning.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), 0 0 0 0 rgba(217, 130, 43, 0), inset 0 0 0 1px #d9822b, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning:focus{
        -webkit-box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #d9822b, 0 0 0 1px #d9822b, 0 0 0 3px rgba(217, 130, 43, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-warning[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #d9822b;
                box-shadow:inset 0 0 0 1px #d9822b; }
      .bp3-dark .bp3-input.bp3-intent-warning:disabled, .bp3-dark .bp3-input.bp3-intent-warning.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input.bp3-intent-danger{
    -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.15), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger:focus{
      -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-input.bp3-intent-danger[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px #db3737;
              box-shadow:inset 0 0 0 1px #db3737; }
    .bp3-input.bp3-intent-danger:disabled, .bp3-input.bp3-intent-danger.bp3-disabled{
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-input.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), 0 0 0 0 rgba(219, 55, 55, 0), inset 0 0 0 1px #db3737, inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger:focus{
        -webkit-box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
                box-shadow:0 0 0 1px #db3737, 0 0 0 1px #db3737, 0 0 0 3px rgba(219, 55, 55, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
      .bp3-dark .bp3-input.bp3-intent-danger[readonly]{
        -webkit-box-shadow:inset 0 0 0 1px #db3737;
                box-shadow:inset 0 0 0 1px #db3737; }
      .bp3-dark .bp3-input.bp3-intent-danger:disabled, .bp3-dark .bp3-input.bp3-intent-danger.bp3-disabled{
        -webkit-box-shadow:none;
                box-shadow:none; }
  .bp3-input::-ms-clear{
    display:none; }
textarea.bp3-input{
  max-width:100%;
  padding:10px; }
  textarea.bp3-input, textarea.bp3-input.bp3-large, textarea.bp3-input.bp3-small{
    height:auto;
    line-height:inherit; }
  textarea.bp3-input.bp3-small{
    padding:8px; }
  .bp3-dark textarea.bp3-input{
    background:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), 0 0 0 0 rgba(19, 124, 189, 0), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark textarea.bp3-input::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input::placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark textarea.bp3-input:focus{
      -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input[readonly]{
      -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark textarea.bp3-input:disabled, .bp3-dark textarea.bp3-input.bp3-disabled{
      background:rgba(57, 75, 89, 0.5);
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
label.bp3-label{
  display:block;
  margin-bottom:15px;
  margin-top:0; }
  label.bp3-label .bp3-html-select,
  label.bp3-label .bp3-input,
  label.bp3-label .bp3-select,
  label.bp3-label .bp3-slider,
  label.bp3-label .bp3-popover-wrapper{
    display:block;
    margin-top:5px;
    text-transform:none; }
  label.bp3-label .bp3-button-group{
    margin-top:5px; }
  label.bp3-label .bp3-select select,
  label.bp3-label .bp3-html-select select{
    font-weight:400;
    vertical-align:top;
    width:100%; }
  label.bp3-label.bp3-disabled,
  label.bp3-label.bp3-disabled .bp3-text-muted{
    color:rgba(92, 112, 128, 0.6); }
  label.bp3-label.bp3-inline{
    line-height:30px; }
    label.bp3-label.bp3-inline .bp3-html-select,
    label.bp3-label.bp3-inline .bp3-input,
    label.bp3-label.bp3-inline .bp3-input-group,
    label.bp3-label.bp3-inline .bp3-select,
    label.bp3-label.bp3-inline .bp3-popover-wrapper{
      display:inline-block;
      margin:0 0 0 5px;
      vertical-align:top; }
    label.bp3-label.bp3-inline .bp3-button-group{
      margin:0 0 0 5px; }
    label.bp3-label.bp3-inline .bp3-input-group .bp3-input{
      margin-left:0; }
    label.bp3-label.bp3-inline.bp3-large{
      line-height:40px; }
  label.bp3-label:not(.bp3-inline) .bp3-popover-target{
    display:block; }
  .bp3-dark label.bp3-label{
    color:#f5f8fa; }
    .bp3-dark label.bp3-label.bp3-disabled,
    .bp3-dark label.bp3-label.bp3-disabled .bp3-text-muted{
      color:rgba(167, 182, 194, 0.6); }
.bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button{
  -webkit-box-flex:1;
      -ms-flex:1 1 14px;
          flex:1 1 14px;
  min-height:0;
  padding:0;
  width:30px; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:first-child{
    border-radius:0 3px 0 0; }
  .bp3-numeric-input .bp3-button-group.bp3-vertical > .bp3-button:last-child{
    border-radius:0 0 3px 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:first-child{
  border-radius:3px 0 0 0; }

.bp3-numeric-input .bp3-button-group.bp3-vertical:first-child > .bp3-button:last-child{
  border-radius:0 0 0 3px; }

.bp3-numeric-input.bp3-large .bp3-button-group.bp3-vertical > .bp3-button{
  width:40px; }

form{
  display:block; }
.bp3-html-select select,
.bp3-select select{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  border:none;
  border-radius:3px;
  cursor:pointer;
  font-size:14px;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  padding:5px 10px;
  text-align:left;
  vertical-align:middle;
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  -moz-appearance:none;
  -webkit-appearance:none;
  border-radius:3px;
  height:30px;
  padding:0 25px 0 10px;
  width:100%; }
  .bp3-html-select select > *, .bp3-select select > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-html-select select > .bp3-fill, .bp3-select select > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-html-select select::before,
  .bp3-select select::before, .bp3-html-select select > *, .bp3-select select > *{
    margin-right:7px; }
  .bp3-html-select select:empty::before,
  .bp3-select select:empty::before,
  .bp3-html-select select > :last-child,
  .bp3-select select > :last-child{
    margin-right:0; }
  .bp3-html-select select:hover,
  .bp3-select select:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-html-select select:active,
  .bp3-select select:active, .bp3-html-select select.bp3-active,
  .bp3-select select.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-html-select select:disabled,
  .bp3-select select:disabled, .bp3-html-select select.bp3-disabled,
  .bp3-select select.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-html-select select:disabled.bp3-active,
    .bp3-select select:disabled.bp3-active, .bp3-html-select select:disabled.bp3-active:hover,
    .bp3-select select:disabled.bp3-active:hover, .bp3-html-select select.bp3-disabled.bp3-active,
    .bp3-select select.bp3-disabled.bp3-active, .bp3-html-select select.bp3-disabled.bp3-active:hover,
    .bp3-select select.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }

.bp3-html-select.bp3-minimal select,
.bp3-select.bp3-minimal select{
  background:none;
  -webkit-box-shadow:none;
          box-shadow:none; }
  .bp3-html-select.bp3-minimal select:hover,
  .bp3-select.bp3-minimal select:hover{
    background:rgba(167, 182, 194, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026;
    text-decoration:none; }
  .bp3-html-select.bp3-minimal select:active,
  .bp3-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal select.bp3-active,
  .bp3-select.bp3-minimal select.bp3-active{
    background:rgba(115, 134, 148, 0.3);
    -webkit-box-shadow:none;
            box-shadow:none;
    color:#182026; }
  .bp3-html-select.bp3-minimal select:disabled,
  .bp3-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal select:disabled:hover,
  .bp3-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal select.bp3-disabled,
  .bp3-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal select.bp3-disabled:hover,
  .bp3-select.bp3-minimal select.bp3-disabled:hover{
    background:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
    .bp3-html-select.bp3-minimal select:disabled.bp3-active,
    .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active,
    .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active{
      background:rgba(115, 134, 148, 0.3); }
  .bp3-dark .bp3-html-select.bp3-minimal select, .bp3-html-select.bp3-minimal .bp3-dark select,
  .bp3-dark .bp3-select.bp3-minimal select, .bp3-select.bp3-minimal .bp3-dark select{
    background:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:inherit; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover, .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none; }
    .bp3-dark .bp3-html-select.bp3-minimal select:hover, .bp3-html-select.bp3-minimal .bp3-dark select:hover,
    .bp3-dark .bp3-select.bp3-minimal select:hover, .bp3-select.bp3-minimal .bp3-dark select:hover{
      background:rgba(138, 155, 168, 0.15); }
    .bp3-dark .bp3-html-select.bp3-minimal select:active, .bp3-html-select.bp3-minimal .bp3-dark select:active,
    .bp3-dark .bp3-select.bp3-minimal select:active, .bp3-select.bp3-minimal .bp3-dark select:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-active,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-active{
      background:rgba(138, 155, 168, 0.3);
      color:#f5f8fa; }
    .bp3-dark .bp3-html-select.bp3-minimal select:disabled, .bp3-html-select.bp3-minimal .bp3-dark select:disabled,
    .bp3-dark .bp3-select.bp3-minimal select:disabled, .bp3-select.bp3-minimal .bp3-dark select:disabled, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select:disabled:hover, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover{
      background:none;
      color:rgba(167, 182, 194, 0.6);
      cursor:not-allowed; }
      .bp3-dark .bp3-html-select.bp3-minimal select:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select:disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select:disabled:hover.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-disabled:hover.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-disabled:hover.bp3-active{
        background:rgba(138, 155, 168, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-primary,
  .bp3-select.bp3-minimal select.bp3-intent-primary{
    color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover,
    .bp3-select.bp3-minimal select.bp3-intent-primary:hover{
      background:rgba(19, 124, 189, 0.15);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:active,
    .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active{
      background:rgba(19, 124, 189, 0.3);
      color:#106ba3; }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled{
      background:none;
      color:rgba(16, 107, 163, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active{
        background:rgba(19, 124, 189, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-primary .bp3-button-spinner .bp3-spinner-head{
      stroke:#106ba3; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary{
      color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:hover{
        background:rgba(19, 124, 189, 0.2);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-active{
        background:rgba(19, 124, 189, 0.3);
        color:#48aff0; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled{
        background:none;
        color:rgba(72, 175, 240, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-primary.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-primary.bp3-disabled.bp3-active{
          background:rgba(19, 124, 189, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-success,
  .bp3-select.bp3-minimal select.bp3-intent-success{
    color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:hover,
    .bp3-select.bp3-minimal select.bp3-intent-success:hover{
      background:rgba(15, 153, 96, 0.15);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:active,
    .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active{
      background:rgba(15, 153, 96, 0.3);
      color:#0d8050; }
    .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled{
      background:none;
      color:rgba(13, 128, 80, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active{
        background:rgba(15, 153, 96, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-success .bp3-button-spinner .bp3-spinner-head{
      stroke:#0d8050; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success{
      color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:hover{
        background:rgba(15, 153, 96, 0.2);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-active{
        background:rgba(15, 153, 96, 0.3);
        color:#3dcc91; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled{
        background:none;
        color:rgba(61, 204, 145, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-success.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-success.bp3-disabled.bp3-active{
          background:rgba(15, 153, 96, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-warning,
  .bp3-select.bp3-minimal select.bp3-intent-warning{
    color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover,
    .bp3-select.bp3-minimal select.bp3-intent-warning:hover{
      background:rgba(217, 130, 43, 0.15);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:active,
    .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active{
      background:rgba(217, 130, 43, 0.3);
      color:#bf7326; }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled{
      background:none;
      color:rgba(191, 115, 38, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active{
        background:rgba(217, 130, 43, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-warning .bp3-button-spinner .bp3-spinner-head{
      stroke:#bf7326; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning{
      color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:hover{
        background:rgba(217, 130, 43, 0.2);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-active{
        background:rgba(217, 130, 43, 0.3);
        color:#ffb366; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled{
        background:none;
        color:rgba(255, 179, 102, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-warning.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-warning.bp3-disabled.bp3-active{
          background:rgba(217, 130, 43, 0.3); }
  .bp3-html-select.bp3-minimal select.bp3-intent-danger,
  .bp3-select.bp3-minimal select.bp3-intent-danger{
    color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover,
    .bp3-select.bp3-minimal select.bp3-intent-danger:hover{
      background:rgba(219, 55, 55, 0.15);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:active,
    .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active{
      background:rgba(219, 55, 55, 0.3);
      color:#c23030; }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled,
    .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled{
      background:none;
      color:rgba(194, 48, 48, 0.5); }
      .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active,
      .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active{
        background:rgba(219, 55, 55, 0.3); }
    .bp3-html-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head, .bp3-select.bp3-minimal select.bp3-intent-danger .bp3-button-spinner .bp3-spinner-head{
      stroke:#c23030; }
    .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger,
    .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger{
      color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:hover, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:hover{
        background:rgba(219, 55, 55, 0.2);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-active{
        background:rgba(219, 55, 55, 0.3);
        color:#ff7373; }
      .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled,
      .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled{
        background:none;
        color:rgba(255, 115, 115, 0.5); }
        .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger:disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger:disabled.bp3-active, .bp3-dark .bp3-html-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-html-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active,
        .bp3-dark .bp3-select.bp3-minimal select.bp3-intent-danger.bp3-disabled.bp3-active, .bp3-select.bp3-minimal .bp3-dark select.bp3-intent-danger.bp3-disabled.bp3-active{
          background:rgba(219, 55, 55, 0.3); }

.bp3-html-select.bp3-large select,
.bp3-select.bp3-large select{
  font-size:16px;
  height:40px;
  padding-right:35px; }

.bp3-dark .bp3-html-select select, .bp3-dark .bp3-select select{
  background-color:#394b59;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
  color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover, .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select select:hover, .bp3-dark .bp3-select select:hover{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-html-select select:active, .bp3-dark .bp3-select select:active, .bp3-dark .bp3-html-select select.bp3-active, .bp3-dark .bp3-select select.bp3-active{
    background-color:#202b33;
    background-image:none;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-html-select select:disabled, .bp3-dark .bp3-select select:disabled, .bp3-dark .bp3-html-select select.bp3-disabled, .bp3-dark .bp3-select select.bp3-disabled{
    background-color:rgba(57, 75, 89, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-html-select select:disabled.bp3-active, .bp3-dark .bp3-select select:disabled.bp3-active, .bp3-dark .bp3-html-select select.bp3-disabled.bp3-active, .bp3-dark .bp3-select select.bp3-disabled.bp3-active{
      background:rgba(57, 75, 89, 0.7); }
  .bp3-dark .bp3-html-select select .bp3-button-spinner .bp3-spinner-head, .bp3-dark .bp3-select select .bp3-button-spinner .bp3-spinner-head{
    background:rgba(16, 22, 26, 0.5);
    stroke:#8a9ba8; }

.bp3-html-select select:disabled,
.bp3-select select:disabled{
  background-color:rgba(206, 217, 224, 0.5);
  -webkit-box-shadow:none;
          box-shadow:none;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-html-select .bp3-icon,
.bp3-select .bp3-icon, .bp3-select::after{
  color:#5c7080;
  pointer-events:none;
  position:absolute;
  right:7px;
  top:7px; }
  .bp3-html-select .bp3-disabled.bp3-icon,
  .bp3-select .bp3-disabled.bp3-icon, .bp3-disabled.bp3-select::after{
    color:rgba(92, 112, 128, 0.6); }
.bp3-html-select,
.bp3-select{
  display:inline-block;
  letter-spacing:normal;
  position:relative;
  vertical-align:middle; }
  .bp3-html-select select::-ms-expand,
  .bp3-select select::-ms-expand{
    display:none; }
  .bp3-html-select .bp3-icon,
  .bp3-select .bp3-icon{
    color:#5c7080; }
    .bp3-html-select .bp3-icon:hover,
    .bp3-select .bp3-icon:hover{
      color:#182026; }
    .bp3-dark .bp3-html-select .bp3-icon, .bp3-dark
    .bp3-select .bp3-icon{
      color:#a7b6c2; }
      .bp3-dark .bp3-html-select .bp3-icon:hover, .bp3-dark
      .bp3-select .bp3-icon:hover{
        color:#f5f8fa; }
  .bp3-html-select.bp3-large::after,
  .bp3-html-select.bp3-large .bp3-icon,
  .bp3-select.bp3-large::after,
  .bp3-select.bp3-large .bp3-icon{
    right:12px;
    top:12px; }
  .bp3-html-select.bp3-fill,
  .bp3-html-select.bp3-fill select,
  .bp3-select.bp3-fill,
  .bp3-select.bp3-fill select{
    width:100%; }
  .bp3-dark .bp3-html-select option, .bp3-dark
  .bp3-select option{
    background-color:#30404d;
    color:#f5f8fa; }
  .bp3-dark .bp3-html-select option:disabled, .bp3-dark
  .bp3-select option:disabled{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-html-select::after, .bp3-dark
  .bp3-select::after{
    color:#a7b6c2; }

.bp3-select::after{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  content:""; }
.bp3-running-text table, table.bp3-html-table{
  border-spacing:0;
  font-size:14px; }
  .bp3-running-text table th, table.bp3-html-table th,
  .bp3-running-text table td,
  table.bp3-html-table td{
    padding:11px;
    text-align:left;
    vertical-align:top; }
  .bp3-running-text table th, table.bp3-html-table th{
    color:#182026;
    font-weight:600; }
  
  .bp3-running-text table td,
  table.bp3-html-table td{
    color:#182026; }
  .bp3-running-text table tbody tr:first-child th, table.bp3-html-table tbody tr:first-child th,
  .bp3-running-text table tbody tr:first-child td,
  table.bp3-html-table tbody tr:first-child td,
  .bp3-running-text table tfoot tr:first-child th,
  table.bp3-html-table tfoot tr:first-child th,
  .bp3-running-text table tfoot tr:first-child td,
  table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  .bp3-dark .bp3-running-text table th, .bp3-running-text .bp3-dark table th, .bp3-dark table.bp3-html-table th{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table td, .bp3-running-text .bp3-dark table td, .bp3-dark table.bp3-html-table td{
    color:#f5f8fa; }
  .bp3-dark .bp3-running-text table tbody tr:first-child th, .bp3-running-text .bp3-dark table tbody tr:first-child th, .bp3-dark table.bp3-html-table tbody tr:first-child th,
  .bp3-dark .bp3-running-text table tbody tr:first-child td,
  .bp3-running-text .bp3-dark table tbody tr:first-child td,
  .bp3-dark table.bp3-html-table tbody tr:first-child td,
  .bp3-dark .bp3-running-text table tfoot tr:first-child th,
  .bp3-running-text .bp3-dark table tfoot tr:first-child th,
  .bp3-dark table.bp3-html-table tfoot tr:first-child th,
  .bp3-dark .bp3-running-text table tfoot tr:first-child td,
  .bp3-running-text .bp3-dark table tfoot tr:first-child td,
  .bp3-dark table.bp3-html-table tfoot tr:first-child td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }

table.bp3-html-table.bp3-html-table-condensed th,
table.bp3-html-table.bp3-html-table-condensed td, table.bp3-html-table.bp3-small th,
table.bp3-html-table.bp3-small td{
  padding-bottom:6px;
  padding-top:6px; }

table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
  background:rgba(191, 204, 214, 0.15); }

table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
  -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered tbody tr td,
table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
  -webkit-box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15);
          box-shadow:inset 0 1px 0 0 rgba(16, 22, 26, 0.15); }
  table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
  table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
    -webkit-box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 1px 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
  -webkit-box-shadow:none;
          box-shadow:none; }
  table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(16, 22, 26, 0.15); }

table.bp3-html-table.bp3-interactive tbody tr:hover td{
  background-color:rgba(191, 204, 214, 0.3);
  cursor:pointer; }

table.bp3-html-table.bp3-interactive tbody tr:active td{
  background-color:rgba(191, 204, 214, 0.4); }

.bp3-dark table.bp3-html-table{ }
  .bp3-dark table.bp3-html-table.bp3-html-table-striped tbody tr:nth-child(odd) td{
    background:rgba(92, 112, 128, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered th:not(:first-child){
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td,
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td{
    -webkit-box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 0 1px 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tbody tr td:not(:first-child),
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered tfoot tr td:not(:first-child){
      -webkit-box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15);
              box-shadow:inset 1px 1px 0 0 rgba(255, 255, 255, 0.15); }
  .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td{
    -webkit-box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15);
            box-shadow:inset 1px 0 0 0 rgba(255, 255, 255, 0.15); }
    .bp3-dark table.bp3-html-table.bp3-html-table-bordered.bp3-html-table-striped tbody tr:not(:first-child) td:first-child{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:hover td{
    background-color:rgba(92, 112, 128, 0.3);
    cursor:pointer; }
  .bp3-dark table.bp3-html-table.bp3-interactive tbody tr:active td{
    background-color:rgba(92, 112, 128, 0.4); }

.bp3-key-combo{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center; }
  .bp3-key-combo > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-key-combo > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-key-combo::before,
  .bp3-key-combo > *{
    margin-right:5px; }
  .bp3-key-combo:empty::before,
  .bp3-key-combo > :last-child{
    margin-right:0; }

.bp3-hotkey-dialog{
  padding-bottom:0;
  top:40px; }
  .bp3-hotkey-dialog .bp3-dialog-body{
    margin:0;
    padding:0; }
  .bp3-hotkey-dialog .bp3-hotkey-label{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1; }

.bp3-hotkey-column{
  margin:auto;
  max-height:80vh;
  overflow-y:auto;
  padding:30px; }
  .bp3-hotkey-column .bp3-heading{
    margin-bottom:20px; }
    .bp3-hotkey-column .bp3-heading:not(:first-child){
      margin-top:40px; }

.bp3-hotkey{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:justify;
      -ms-flex-pack:justify;
          justify-content:space-between;
  margin-left:0;
  margin-right:0; }
  .bp3-hotkey:not(:last-child){
    margin-bottom:10px; }
.bp3-icon{
  display:inline-block;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  vertical-align:text-bottom; }
  .bp3-icon:not(:empty)::before{
    content:"" !important;
    content:unset !important; }
  .bp3-icon > svg{
    display:block; }
    .bp3-icon > svg:not([fill]){
      fill:currentColor; }

.bp3-icon.bp3-intent-primary, .bp3-icon-standard.bp3-intent-primary, .bp3-icon-large.bp3-intent-primary{
  color:#106ba3; }
  .bp3-dark .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-icon-large.bp3-intent-primary{
    color:#48aff0; }

.bp3-icon.bp3-intent-success, .bp3-icon-standard.bp3-intent-success, .bp3-icon-large.bp3-intent-success{
  color:#0d8050; }
  .bp3-dark .bp3-icon.bp3-intent-success, .bp3-dark .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-icon-large.bp3-intent-success{
    color:#3dcc91; }

.bp3-icon.bp3-intent-warning, .bp3-icon-standard.bp3-intent-warning, .bp3-icon-large.bp3-intent-warning{
  color:#bf7326; }
  .bp3-dark .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-icon-large.bp3-intent-warning{
    color:#ffb366; }

.bp3-icon.bp3-intent-danger, .bp3-icon-standard.bp3-intent-danger, .bp3-icon-large.bp3-intent-danger{
  color:#c23030; }
  .bp3-dark .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-icon-large.bp3-intent-danger{
    color:#ff7373; }

span.bp3-icon-standard{
  font-family:"Icons16", sans-serif;
  font-size:16px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon-large{
  font-family:"Icons20", sans-serif;
  font-size:20px;
  font-style:normal;
  font-weight:400;
  line-height:1;
  -moz-osx-font-smoothing:grayscale;
  -webkit-font-smoothing:antialiased;
  display:inline-block; }

span.bp3-icon:empty{
  font-family:"Icons20";
  font-size:inherit;
  font-style:normal;
  font-weight:400;
  line-height:1; }
  span.bp3-icon:empty::before{
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased; }

.bp3-icon-add::before{
  content:""; }

.bp3-icon-add-column-left::before{
  content:""; }

.bp3-icon-add-column-right::before{
  content:""; }

.bp3-icon-add-row-bottom::before{
  content:""; }

.bp3-icon-add-row-top::before{
  content:""; }

.bp3-icon-add-to-artifact::before{
  content:""; }

.bp3-icon-add-to-folder::before{
  content:""; }

.bp3-icon-airplane::before{
  content:""; }

.bp3-icon-align-center::before{
  content:""; }

.bp3-icon-align-justify::before{
  content:""; }

.bp3-icon-align-left::before{
  content:""; }

.bp3-icon-align-right::before{
  content:""; }

.bp3-icon-alignment-bottom::before{
  content:""; }

.bp3-icon-alignment-horizontal-center::before{
  content:""; }

.bp3-icon-alignment-left::before{
  content:""; }

.bp3-icon-alignment-right::before{
  content:""; }

.bp3-icon-alignment-top::before{
  content:""; }

.bp3-icon-alignment-vertical-center::before{
  content:""; }

.bp3-icon-annotation::before{
  content:""; }

.bp3-icon-application::before{
  content:""; }

.bp3-icon-applications::before{
  content:""; }

.bp3-icon-archive::before{
  content:""; }

.bp3-icon-arrow-bottom-left::before{
  content:"↙"; }

.bp3-icon-arrow-bottom-right::before{
  content:"↘"; }

.bp3-icon-arrow-down::before{
  content:"↓"; }

.bp3-icon-arrow-left::before{
  content:"←"; }

.bp3-icon-arrow-right::before{
  content:"→"; }

.bp3-icon-arrow-top-left::before{
  content:"↖"; }

.bp3-icon-arrow-top-right::before{
  content:"↗"; }

.bp3-icon-arrow-up::before{
  content:"↑"; }

.bp3-icon-arrows-horizontal::before{
  content:"↔"; }

.bp3-icon-arrows-vertical::before{
  content:"↕"; }

.bp3-icon-asterisk::before{
  content:"*"; }

.bp3-icon-automatic-updates::before{
  content:""; }

.bp3-icon-badge::before{
  content:""; }

.bp3-icon-ban-circle::before{
  content:""; }

.bp3-icon-bank-account::before{
  content:""; }

.bp3-icon-barcode::before{
  content:""; }

.bp3-icon-blank::before{
  content:""; }

.bp3-icon-blocked-person::before{
  content:""; }

.bp3-icon-bold::before{
  content:""; }

.bp3-icon-book::before{
  content:""; }

.bp3-icon-bookmark::before{
  content:""; }

.bp3-icon-box::before{
  content:""; }

.bp3-icon-briefcase::before{
  content:""; }

.bp3-icon-bring-data::before{
  content:""; }

.bp3-icon-build::before{
  content:""; }

.bp3-icon-calculator::before{
  content:""; }

.bp3-icon-calendar::before{
  content:""; }

.bp3-icon-camera::before{
  content:""; }

.bp3-icon-caret-down::before{
  content:"⌄"; }

.bp3-icon-caret-left::before{
  content:"〈"; }

.bp3-icon-caret-right::before{
  content:"〉"; }

.bp3-icon-caret-up::before{
  content:"⌃"; }

.bp3-icon-cell-tower::before{
  content:""; }

.bp3-icon-changes::before{
  content:""; }

.bp3-icon-chart::before{
  content:""; }

.bp3-icon-chat::before{
  content:""; }

.bp3-icon-chevron-backward::before{
  content:""; }

.bp3-icon-chevron-down::before{
  content:""; }

.bp3-icon-chevron-forward::before{
  content:""; }

.bp3-icon-chevron-left::before{
  content:""; }

.bp3-icon-chevron-right::before{
  content:""; }

.bp3-icon-chevron-up::before{
  content:""; }

.bp3-icon-circle::before{
  content:""; }

.bp3-icon-circle-arrow-down::before{
  content:""; }

.bp3-icon-circle-arrow-left::before{
  content:""; }

.bp3-icon-circle-arrow-right::before{
  content:""; }

.bp3-icon-circle-arrow-up::before{
  content:""; }

.bp3-icon-citation::before{
  content:""; }

.bp3-icon-clean::before{
  content:""; }

.bp3-icon-clipboard::before{
  content:""; }

.bp3-icon-cloud::before{
  content:"☁"; }

.bp3-icon-cloud-download::before{
  content:""; }

.bp3-icon-cloud-upload::before{
  content:""; }

.bp3-icon-code::before{
  content:""; }

.bp3-icon-code-block::before{
  content:""; }

.bp3-icon-cog::before{
  content:""; }

.bp3-icon-collapse-all::before{
  content:""; }

.bp3-icon-column-layout::before{
  content:""; }

.bp3-icon-comment::before{
  content:""; }

.bp3-icon-comparison::before{
  content:""; }

.bp3-icon-compass::before{
  content:""; }

.bp3-icon-compressed::before{
  content:""; }

.bp3-icon-confirm::before{
  content:""; }

.bp3-icon-console::before{
  content:""; }

.bp3-icon-contrast::before{
  content:""; }

.bp3-icon-control::before{
  content:""; }

.bp3-icon-credit-card::before{
  content:""; }

.bp3-icon-cross::before{
  content:"✗"; }

.bp3-icon-crown::before{
  content:""; }

.bp3-icon-cube::before{
  content:""; }

.bp3-icon-cube-add::before{
  content:""; }

.bp3-icon-cube-remove::before{
  content:""; }

.bp3-icon-curved-range-chart::before{
  content:""; }

.bp3-icon-cut::before{
  content:""; }

.bp3-icon-dashboard::before{
  content:""; }

.bp3-icon-data-lineage::before{
  content:""; }

.bp3-icon-database::before{
  content:""; }

.bp3-icon-delete::before{
  content:""; }

.bp3-icon-delta::before{
  content:"Δ"; }

.bp3-icon-derive-column::before{
  content:""; }

.bp3-icon-desktop::before{
  content:""; }

.bp3-icon-diagnosis::before{
  content:""; }

.bp3-icon-diagram-tree::before{
  content:""; }

.bp3-icon-direction-left::before{
  content:""; }

.bp3-icon-direction-right::before{
  content:""; }

.bp3-icon-disable::before{
  content:""; }

.bp3-icon-document::before{
  content:""; }

.bp3-icon-document-open::before{
  content:""; }

.bp3-icon-document-share::before{
  content:""; }

.bp3-icon-dollar::before{
  content:"$"; }

.bp3-icon-dot::before{
  content:"•"; }

.bp3-icon-double-caret-horizontal::before{
  content:""; }

.bp3-icon-double-caret-vertical::before{
  content:""; }

.bp3-icon-double-chevron-down::before{
  content:""; }

.bp3-icon-double-chevron-left::before{
  content:""; }

.bp3-icon-double-chevron-right::before{
  content:""; }

.bp3-icon-double-chevron-up::before{
  content:""; }

.bp3-icon-doughnut-chart::before{
  content:""; }

.bp3-icon-download::before{
  content:""; }

.bp3-icon-drag-handle-horizontal::before{
  content:""; }

.bp3-icon-drag-handle-vertical::before{
  content:""; }

.bp3-icon-draw::before{
  content:""; }

.bp3-icon-drive-time::before{
  content:""; }

.bp3-icon-duplicate::before{
  content:""; }

.bp3-icon-edit::before{
  content:"✎"; }

.bp3-icon-eject::before{
  content:"⏏"; }

.bp3-icon-endorsed::before{
  content:""; }

.bp3-icon-envelope::before{
  content:"✉"; }

.bp3-icon-equals::before{
  content:""; }

.bp3-icon-eraser::before{
  content:""; }

.bp3-icon-error::before{
  content:""; }

.bp3-icon-euro::before{
  content:"€"; }

.bp3-icon-exchange::before{
  content:""; }

.bp3-icon-exclude-row::before{
  content:""; }

.bp3-icon-expand-all::before{
  content:""; }

.bp3-icon-export::before{
  content:""; }

.bp3-icon-eye-off::before{
  content:""; }

.bp3-icon-eye-on::before{
  content:""; }

.bp3-icon-eye-open::before{
  content:""; }

.bp3-icon-fast-backward::before{
  content:""; }

.bp3-icon-fast-forward::before{
  content:""; }

.bp3-icon-feed::before{
  content:""; }

.bp3-icon-feed-subscribed::before{
  content:""; }

.bp3-icon-film::before{
  content:""; }

.bp3-icon-filter::before{
  content:""; }

.bp3-icon-filter-keep::before{
  content:""; }

.bp3-icon-filter-list::before{
  content:""; }

.bp3-icon-filter-open::before{
  content:""; }

.bp3-icon-filter-remove::before{
  content:""; }

.bp3-icon-flag::before{
  content:"⚑"; }

.bp3-icon-flame::before{
  content:""; }

.bp3-icon-flash::before{
  content:""; }

.bp3-icon-floppy-disk::before{
  content:""; }

.bp3-icon-flow-branch::before{
  content:""; }

.bp3-icon-flow-end::before{
  content:""; }

.bp3-icon-flow-linear::before{
  content:""; }

.bp3-icon-flow-review::before{
  content:""; }

.bp3-icon-flow-review-branch::before{
  content:""; }

.bp3-icon-flows::before{
  content:""; }

.bp3-icon-folder-close::before{
  content:""; }

.bp3-icon-folder-new::before{
  content:""; }

.bp3-icon-folder-open::before{
  content:""; }

.bp3-icon-folder-shared::before{
  content:""; }

.bp3-icon-folder-shared-open::before{
  content:""; }

.bp3-icon-follower::before{
  content:""; }

.bp3-icon-following::before{
  content:""; }

.bp3-icon-font::before{
  content:""; }

.bp3-icon-fork::before{
  content:""; }

.bp3-icon-form::before{
  content:""; }

.bp3-icon-full-circle::before{
  content:""; }

.bp3-icon-full-stacked-chart::before{
  content:""; }

.bp3-icon-fullscreen::before{
  content:""; }

.bp3-icon-function::before{
  content:""; }

.bp3-icon-gantt-chart::before{
  content:""; }

.bp3-icon-geolocation::before{
  content:""; }

.bp3-icon-geosearch::before{
  content:""; }

.bp3-icon-git-branch::before{
  content:""; }

.bp3-icon-git-commit::before{
  content:""; }

.bp3-icon-git-merge::before{
  content:""; }

.bp3-icon-git-new-branch::before{
  content:""; }

.bp3-icon-git-pull::before{
  content:""; }

.bp3-icon-git-push::before{
  content:""; }

.bp3-icon-git-repo::before{
  content:""; }

.bp3-icon-glass::before{
  content:""; }

.bp3-icon-globe::before{
  content:""; }

.bp3-icon-globe-network::before{
  content:""; }

.bp3-icon-graph::before{
  content:""; }

.bp3-icon-graph-remove::before{
  content:""; }

.bp3-icon-greater-than::before{
  content:""; }

.bp3-icon-greater-than-or-equal-to::before{
  content:""; }

.bp3-icon-grid::before{
  content:""; }

.bp3-icon-grid-view::before{
  content:""; }

.bp3-icon-group-objects::before{
  content:""; }

.bp3-icon-grouped-bar-chart::before{
  content:""; }

.bp3-icon-hand::before{
  content:""; }

.bp3-icon-hand-down::before{
  content:""; }

.bp3-icon-hand-left::before{
  content:""; }

.bp3-icon-hand-right::before{
  content:""; }

.bp3-icon-hand-up::before{
  content:""; }

.bp3-icon-header::before{
  content:""; }

.bp3-icon-header-one::before{
  content:""; }

.bp3-icon-header-two::before{
  content:""; }

.bp3-icon-headset::before{
  content:""; }

.bp3-icon-heart::before{
  content:"♥"; }

.bp3-icon-heart-broken::before{
  content:""; }

.bp3-icon-heat-grid::before{
  content:""; }

.bp3-icon-heatmap::before{
  content:""; }

.bp3-icon-help::before{
  content:"?"; }

.bp3-icon-helper-management::before{
  content:""; }

.bp3-icon-highlight::before{
  content:""; }

.bp3-icon-history::before{
  content:""; }

.bp3-icon-home::before{
  content:"⌂"; }

.bp3-icon-horizontal-bar-chart::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-asc::before{
  content:""; }

.bp3-icon-horizontal-bar-chart-desc::before{
  content:""; }

.bp3-icon-horizontal-distribution::before{
  content:""; }

.bp3-icon-id-number::before{
  content:""; }

.bp3-icon-image-rotate-left::before{
  content:""; }

.bp3-icon-image-rotate-right::before{
  content:""; }

.bp3-icon-import::before{
  content:""; }

.bp3-icon-inbox::before{
  content:""; }

.bp3-icon-inbox-filtered::before{
  content:""; }

.bp3-icon-inbox-geo::before{
  content:""; }

.bp3-icon-inbox-search::before{
  content:""; }

.bp3-icon-inbox-update::before{
  content:""; }

.bp3-icon-info-sign::before{
  content:"ℹ"; }

.bp3-icon-inheritance::before{
  content:""; }

.bp3-icon-inner-join::before{
  content:""; }

.bp3-icon-insert::before{
  content:""; }

.bp3-icon-intersection::before{
  content:""; }

.bp3-icon-ip-address::before{
  content:""; }

.bp3-icon-issue::before{
  content:""; }

.bp3-icon-issue-closed::before{
  content:""; }

.bp3-icon-issue-new::before{
  content:""; }

.bp3-icon-italic::before{
  content:""; }

.bp3-icon-join-table::before{
  content:""; }

.bp3-icon-key::before{
  content:""; }

.bp3-icon-key-backspace::before{
  content:""; }

.bp3-icon-key-command::before{
  content:""; }

.bp3-icon-key-control::before{
  content:""; }

.bp3-icon-key-delete::before{
  content:""; }

.bp3-icon-key-enter::before{
  content:""; }

.bp3-icon-key-escape::before{
  content:""; }

.bp3-icon-key-option::before{
  content:""; }

.bp3-icon-key-shift::before{
  content:""; }

.bp3-icon-key-tab::before{
  content:""; }

.bp3-icon-known-vehicle::before{
  content:""; }

.bp3-icon-lab-test::before{
  content:""; }

.bp3-icon-label::before{
  content:""; }

.bp3-icon-layer::before{
  content:""; }

.bp3-icon-layers::before{
  content:""; }

.bp3-icon-layout::before{
  content:""; }

.bp3-icon-layout-auto::before{
  content:""; }

.bp3-icon-layout-balloon::before{
  content:""; }

.bp3-icon-layout-circle::before{
  content:""; }

.bp3-icon-layout-grid::before{
  content:""; }

.bp3-icon-layout-group-by::before{
  content:""; }

.bp3-icon-layout-hierarchy::before{
  content:""; }

.bp3-icon-layout-linear::before{
  content:""; }

.bp3-icon-layout-skew-grid::before{
  content:""; }

.bp3-icon-layout-sorted-clusters::before{
  content:""; }

.bp3-icon-learning::before{
  content:""; }

.bp3-icon-left-join::before{
  content:""; }

.bp3-icon-less-than::before{
  content:""; }

.bp3-icon-less-than-or-equal-to::before{
  content:""; }

.bp3-icon-lifesaver::before{
  content:""; }

.bp3-icon-lightbulb::before{
  content:""; }

.bp3-icon-link::before{
  content:""; }

.bp3-icon-list::before{
  content:"☰"; }

.bp3-icon-list-columns::before{
  content:""; }

.bp3-icon-list-detail-view::before{
  content:""; }

.bp3-icon-locate::before{
  content:""; }

.bp3-icon-lock::before{
  content:""; }

.bp3-icon-log-in::before{
  content:""; }

.bp3-icon-log-out::before{
  content:""; }

.bp3-icon-manual::before{
  content:""; }

.bp3-icon-manually-entered-data::before{
  content:""; }

.bp3-icon-map::before{
  content:""; }

.bp3-icon-map-create::before{
  content:""; }

.bp3-icon-map-marker::before{
  content:""; }

.bp3-icon-maximize::before{
  content:""; }

.bp3-icon-media::before{
  content:""; }

.bp3-icon-menu::before{
  content:""; }

.bp3-icon-menu-closed::before{
  content:""; }

.bp3-icon-menu-open::before{
  content:""; }

.bp3-icon-merge-columns::before{
  content:""; }

.bp3-icon-merge-links::before{
  content:""; }

.bp3-icon-minimize::before{
  content:""; }

.bp3-icon-minus::before{
  content:"−"; }

.bp3-icon-mobile-phone::before{
  content:""; }

.bp3-icon-mobile-video::before{
  content:""; }

.bp3-icon-moon::before{
  content:""; }

.bp3-icon-more::before{
  content:""; }

.bp3-icon-mountain::before{
  content:""; }

.bp3-icon-move::before{
  content:""; }

.bp3-icon-mugshot::before{
  content:""; }

.bp3-icon-multi-select::before{
  content:""; }

.bp3-icon-music::before{
  content:""; }

.bp3-icon-new-drawing::before{
  content:""; }

.bp3-icon-new-grid-item::before{
  content:""; }

.bp3-icon-new-layer::before{
  content:""; }

.bp3-icon-new-layers::before{
  content:""; }

.bp3-icon-new-link::before{
  content:""; }

.bp3-icon-new-object::before{
  content:""; }

.bp3-icon-new-person::before{
  content:""; }

.bp3-icon-new-prescription::before{
  content:""; }

.bp3-icon-new-text-box::before{
  content:""; }

.bp3-icon-ninja::before{
  content:""; }

.bp3-icon-not-equal-to::before{
  content:""; }

.bp3-icon-notifications::before{
  content:""; }

.bp3-icon-notifications-updated::before{
  content:""; }

.bp3-icon-numbered-list::before{
  content:""; }

.bp3-icon-numerical::before{
  content:""; }

.bp3-icon-office::before{
  content:""; }

.bp3-icon-offline::before{
  content:""; }

.bp3-icon-oil-field::before{
  content:""; }

.bp3-icon-one-column::before{
  content:""; }

.bp3-icon-outdated::before{
  content:""; }

.bp3-icon-page-layout::before{
  content:""; }

.bp3-icon-panel-stats::before{
  content:""; }

.bp3-icon-panel-table::before{
  content:""; }

.bp3-icon-paperclip::before{
  content:""; }

.bp3-icon-paragraph::before{
  content:""; }

.bp3-icon-path::before{
  content:""; }

.bp3-icon-path-search::before{
  content:""; }

.bp3-icon-pause::before{
  content:""; }

.bp3-icon-people::before{
  content:""; }

.bp3-icon-percentage::before{
  content:""; }

.bp3-icon-person::before{
  content:""; }

.bp3-icon-phone::before{
  content:"☎"; }

.bp3-icon-pie-chart::before{
  content:""; }

.bp3-icon-pin::before{
  content:""; }

.bp3-icon-pivot::before{
  content:""; }

.bp3-icon-pivot-table::before{
  content:""; }

.bp3-icon-play::before{
  content:""; }

.bp3-icon-plus::before{
  content:"+"; }

.bp3-icon-polygon-filter::before{
  content:""; }

.bp3-icon-power::before{
  content:""; }

.bp3-icon-predictive-analysis::before{
  content:""; }

.bp3-icon-prescription::before{
  content:""; }

.bp3-icon-presentation::before{
  content:""; }

.bp3-icon-print::before{
  content:"⎙"; }

.bp3-icon-projects::before{
  content:""; }

.bp3-icon-properties::before{
  content:""; }

.bp3-icon-property::before{
  content:""; }

.bp3-icon-publish-function::before{
  content:""; }

.bp3-icon-pulse::before{
  content:""; }

.bp3-icon-random::before{
  content:""; }

.bp3-icon-record::before{
  content:""; }

.bp3-icon-redo::before{
  content:""; }

.bp3-icon-refresh::before{
  content:""; }

.bp3-icon-regression-chart::before{
  content:""; }

.bp3-icon-remove::before{
  content:""; }

.bp3-icon-remove-column::before{
  content:""; }

.bp3-icon-remove-column-left::before{
  content:""; }

.bp3-icon-remove-column-right::before{
  content:""; }

.bp3-icon-remove-row-bottom::before{
  content:""; }

.bp3-icon-remove-row-top::before{
  content:""; }

.bp3-icon-repeat::before{
  content:""; }

.bp3-icon-reset::before{
  content:""; }

.bp3-icon-resolve::before{
  content:""; }

.bp3-icon-rig::before{
  content:""; }

.bp3-icon-right-join::before{
  content:""; }

.bp3-icon-ring::before{
  content:""; }

.bp3-icon-rotate-document::before{
  content:""; }

.bp3-icon-rotate-page::before{
  content:""; }

.bp3-icon-satellite::before{
  content:""; }

.bp3-icon-saved::before{
  content:""; }

.bp3-icon-scatter-plot::before{
  content:""; }

.bp3-icon-search::before{
  content:""; }

.bp3-icon-search-around::before{
  content:""; }

.bp3-icon-search-template::before{
  content:""; }

.bp3-icon-search-text::before{
  content:""; }

.bp3-icon-segmented-control::before{
  content:""; }

.bp3-icon-select::before{
  content:""; }

.bp3-icon-selection::before{
  content:"⦿"; }

.bp3-icon-send-to::before{
  content:""; }

.bp3-icon-send-to-graph::before{
  content:""; }

.bp3-icon-send-to-map::before{
  content:""; }

.bp3-icon-series-add::before{
  content:""; }

.bp3-icon-series-configuration::before{
  content:""; }

.bp3-icon-series-derived::before{
  content:""; }

.bp3-icon-series-filtered::before{
  content:""; }

.bp3-icon-series-search::before{
  content:""; }

.bp3-icon-settings::before{
  content:""; }

.bp3-icon-share::before{
  content:""; }

.bp3-icon-shield::before{
  content:""; }

.bp3-icon-shop::before{
  content:""; }

.bp3-icon-shopping-cart::before{
  content:""; }

.bp3-icon-signal-search::before{
  content:""; }

.bp3-icon-sim-card::before{
  content:""; }

.bp3-icon-slash::before{
  content:""; }

.bp3-icon-small-cross::before{
  content:""; }

.bp3-icon-small-minus::before{
  content:""; }

.bp3-icon-small-plus::before{
  content:""; }

.bp3-icon-small-tick::before{
  content:""; }

.bp3-icon-snowflake::before{
  content:""; }

.bp3-icon-social-media::before{
  content:""; }

.bp3-icon-sort::before{
  content:""; }

.bp3-icon-sort-alphabetical::before{
  content:""; }

.bp3-icon-sort-alphabetical-desc::before{
  content:""; }

.bp3-icon-sort-asc::before{
  content:""; }

.bp3-icon-sort-desc::before{
  content:""; }

.bp3-icon-sort-numerical::before{
  content:""; }

.bp3-icon-sort-numerical-desc::before{
  content:""; }

.bp3-icon-split-columns::before{
  content:""; }

.bp3-icon-square::before{
  content:""; }

.bp3-icon-stacked-chart::before{
  content:""; }

.bp3-icon-star::before{
  content:"★"; }

.bp3-icon-star-empty::before{
  content:"☆"; }

.bp3-icon-step-backward::before{
  content:""; }

.bp3-icon-step-chart::before{
  content:""; }

.bp3-icon-step-forward::before{
  content:""; }

.bp3-icon-stop::before{
  content:""; }

.bp3-icon-stopwatch::before{
  content:""; }

.bp3-icon-strikethrough::before{
  content:""; }

.bp3-icon-style::before{
  content:""; }

.bp3-icon-swap-horizontal::before{
  content:""; }

.bp3-icon-swap-vertical::before{
  content:""; }

.bp3-icon-symbol-circle::before{
  content:""; }

.bp3-icon-symbol-cross::before{
  content:""; }

.bp3-icon-symbol-diamond::before{
  content:""; }

.bp3-icon-symbol-square::before{
  content:""; }

.bp3-icon-symbol-triangle-down::before{
  content:""; }

.bp3-icon-symbol-triangle-up::before{
  content:""; }

.bp3-icon-tag::before{
  content:""; }

.bp3-icon-take-action::before{
  content:""; }

.bp3-icon-taxi::before{
  content:""; }

.bp3-icon-text-highlight::before{
  content:""; }

.bp3-icon-th::before{
  content:""; }

.bp3-icon-th-derived::before{
  content:""; }

.bp3-icon-th-disconnect::before{
  content:""; }

.bp3-icon-th-filtered::before{
  content:""; }

.bp3-icon-th-list::before{
  content:""; }

.bp3-icon-thumbs-down::before{
  content:""; }

.bp3-icon-thumbs-up::before{
  content:""; }

.bp3-icon-tick::before{
  content:"✓"; }

.bp3-icon-tick-circle::before{
  content:""; }

.bp3-icon-time::before{
  content:"⏲"; }

.bp3-icon-timeline-area-chart::before{
  content:""; }

.bp3-icon-timeline-bar-chart::before{
  content:""; }

.bp3-icon-timeline-events::before{
  content:""; }

.bp3-icon-timeline-line-chart::before{
  content:""; }

.bp3-icon-tint::before{
  content:""; }

.bp3-icon-torch::before{
  content:""; }

.bp3-icon-tractor::before{
  content:""; }

.bp3-icon-train::before{
  content:""; }

.bp3-icon-translate::before{
  content:""; }

.bp3-icon-trash::before{
  content:""; }

.bp3-icon-tree::before{
  content:""; }

.bp3-icon-trending-down::before{
  content:""; }

.bp3-icon-trending-up::before{
  content:""; }

.bp3-icon-truck::before{
  content:""; }

.bp3-icon-two-columns::before{
  content:""; }

.bp3-icon-unarchive::before{
  content:""; }

.bp3-icon-underline::before{
  content:"⎁"; }

.bp3-icon-undo::before{
  content:"⎌"; }

.bp3-icon-ungroup-objects::before{
  content:""; }

.bp3-icon-unknown-vehicle::before{
  content:""; }

.bp3-icon-unlock::before{
  content:""; }

.bp3-icon-unpin::before{
  content:""; }

.bp3-icon-unresolve::before{
  content:""; }

.bp3-icon-updated::before{
  content:""; }

.bp3-icon-upload::before{
  content:""; }

.bp3-icon-user::before{
  content:""; }

.bp3-icon-variable::before{
  content:""; }

.bp3-icon-vertical-bar-chart-asc::before{
  content:""; }

.bp3-icon-vertical-bar-chart-desc::before{
  content:""; }

.bp3-icon-vertical-distribution::before{
  content:""; }

.bp3-icon-video::before{
  content:""; }

.bp3-icon-volume-down::before{
  content:""; }

.bp3-icon-volume-off::before{
  content:""; }

.bp3-icon-volume-up::before{
  content:""; }

.bp3-icon-walk::before{
  content:""; }

.bp3-icon-warning-sign::before{
  content:""; }

.bp3-icon-waterfall-chart::before{
  content:""; }

.bp3-icon-widget::before{
  content:""; }

.bp3-icon-widget-button::before{
  content:""; }

.bp3-icon-widget-footer::before{
  content:""; }

.bp3-icon-widget-header::before{
  content:""; }

.bp3-icon-wrench::before{
  content:""; }

.bp3-icon-zoom-in::before{
  content:""; }

.bp3-icon-zoom-out::before{
  content:""; }

.bp3-icon-zoom-to-fit::before{
  content:""; }
.bp3-submenu > .bp3-popover-wrapper{
  display:block; }

.bp3-submenu .bp3-popover-target{
  display:block; }
  .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{ }

.bp3-submenu.bp3-popover{
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0 5px; }
  .bp3-submenu.bp3-popover > .bp3-popover-content{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-submenu.bp3-popover, .bp3-submenu.bp3-popover.bp3-dark{
    -webkit-box-shadow:none;
            box-shadow:none; }
    .bp3-dark .bp3-submenu.bp3-popover > .bp3-popover-content, .bp3-submenu.bp3-popover.bp3-dark > .bp3-popover-content{
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
.bp3-menu{
  background:#ffffff;
  border-radius:3px;
  color:#182026;
  list-style:none;
  margin:0;
  min-width:180px;
  padding:5px;
  text-align:left; }

.bp3-menu-divider{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px; }
  .bp3-dark .bp3-menu-divider{
    border-top-color:rgba(255, 255, 255, 0.15); }

.bp3-menu-item{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  border-radius:2px;
  color:inherit;
  line-height:20px;
  padding:5px 7px;
  text-decoration:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-menu-item > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-menu-item > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-menu-item::before,
  .bp3-menu-item > *{
    margin-right:7px; }
  .bp3-menu-item:empty::before,
  .bp3-menu-item > :last-child{
    margin-right:0; }
  .bp3-menu-item > .bp3-fill{
    word-break:break-word; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    background-color:rgba(167, 182, 194, 0.3);
    cursor:pointer;
    text-decoration:none; }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-dark .bp3-menu-item{
    color:inherit; }
    .bp3-dark .bp3-menu-item:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
      background-color:rgba(138, 155, 168, 0.15);
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-disabled{
      background-color:inherit;
      color:rgba(167, 182, 194, 0.6); }
  .bp3-menu-item.bp3-intent-primary{
    color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-primary::before, .bp3-menu-item.bp3-intent-primary::after,
    .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-menu-item.bp3-intent-primary:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary:active, .bp3-menu-item.bp3-intent-primary:active::before, .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-success{
    color:#0d8050; }
    .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-success::before, .bp3-menu-item.bp3-intent-success::after,
    .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-menu-item.bp3-intent-success:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-menu-item.bp3-intent-success:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-menu-item.bp3-intent-success:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success:active, .bp3-menu-item.bp3-intent-success:active::before, .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-warning{
    color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-warning::before, .bp3-menu-item.bp3-intent-warning::after,
    .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-menu-item.bp3-intent-warning:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning:active, .bp3-menu-item.bp3-intent-warning:active::before, .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item.bp3-intent-danger{
    color:#c23030; }
    .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-menu-item.bp3-intent-danger::before, .bp3-menu-item.bp3-intent-danger::after,
    .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-menu-item.bp3-intent-danger:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger:active, .bp3-menu-item.bp3-intent-danger:active::before, .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-menu-item::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    margin-right:7px; }
  .bp3-menu-item::before,
  .bp3-menu-item > .bp3-icon{
    color:#5c7080;
    margin-top:2px; }
  .bp3-menu-item .bp3-menu-item-label{
    color:#5c7080; }
  .bp3-menu-item:hover, .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-menu-item{
    color:inherit; }
  .bp3-menu-item.bp3-active, .bp3-menu-item:active{
    background-color:rgba(115, 134, 148, 0.3); }
  .bp3-menu-item.bp3-disabled{
    background-color:inherit !important;
    color:rgba(92, 112, 128, 0.6) !important;
    cursor:not-allowed !important;
    outline:none !important; }
    .bp3-menu-item.bp3-disabled::before,
    .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(92, 112, 128, 0.6) !important; }
  .bp3-large .bp3-menu-item{
    font-size:16px;
    line-height:22px;
    padding:9px 7px; }
    .bp3-large .bp3-menu-item .bp3-icon{
      margin-top:3px; }
    .bp3-large .bp3-menu-item::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1;
      -moz-osx-font-smoothing:grayscale;
      -webkit-font-smoothing:antialiased;
      margin-right:10px;
      margin-top:1px; }

button.bp3-menu-item{
  background:none;
  border:none;
  text-align:left;
  width:100%; }
.bp3-menu-header{
  border-top:1px solid rgba(16, 22, 26, 0.15);
  display:block;
  margin:5px;
  cursor:default;
  padding-left:2px; }
  .bp3-dark .bp3-menu-header{
    border-top-color:rgba(255, 255, 255, 0.15); }
  .bp3-menu-header:first-of-type{
    border-top:none; }
  .bp3-menu-header > h6{
    color:#182026;
    font-weight:600;
    overflow:hidden;
    text-overflow:ellipsis;
    white-space:nowrap;
    word-wrap:normal;
    line-height:17px;
    margin:0;
    padding:10px 7px 0 1px; }
    .bp3-dark .bp3-menu-header > h6{
      color:#f5f8fa; }
  .bp3-menu-header:first-of-type > h6{
    padding-top:0; }
  .bp3-large .bp3-menu-header > h6{
    font-size:18px;
    padding-bottom:5px;
    padding-top:15px; }
  .bp3-large .bp3-menu-header:first-of-type > h6{
    padding-top:0; }

.bp3-dark .bp3-menu{
  background:#30404d;
  color:#f5f8fa; }

.bp3-dark .bp3-menu-item{ }
  .bp3-dark .bp3-menu-item.bp3-intent-primary{
    color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary::before, .bp3-dark .bp3-menu-item.bp3-intent-primary::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary .bp3-menu-item-label{
      color:#48aff0; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active{
      background-color:#137cbd; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active{
      background-color:#106ba3; }
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-primary.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary:active, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-primary.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-success{
    color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-success::before, .bp3-dark .bp3-menu-item.bp3-intent-success::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success .bp3-menu-item-label{
      color:#3dcc91; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active{
      background-color:#0f9960; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:active{
      background-color:#0d8050; }
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-success:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-success.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success:active, .bp3-dark .bp3-menu-item.bp3-intent-success:active::before, .bp3-dark .bp3-menu-item.bp3-intent-success:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-success.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-warning{
    color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning::before, .bp3-dark .bp3-menu-item.bp3-intent-warning::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning .bp3-menu-item-label{
      color:#ffb366; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active{
      background-color:#d9822b; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active{
      background-color:#bf7326; }
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-warning.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning:active, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-warning.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item.bp3-intent-danger{
    color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-icon{
      color:inherit; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger::before, .bp3-dark .bp3-menu-item.bp3-intent-danger::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger .bp3-menu-item-label{
      color:#ff7373; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active{
      background-color:#db3737; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active{
      background-color:#c23030; }
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::before, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:hover::after, .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after, .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:hover .bp3-menu-item-label,
    .bp3-dark .bp3-submenu .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label,
    .bp3-submenu .bp3-dark .bp3-popover-target.bp3-popover-open > .bp3-intent-danger.bp3-menu-item .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger:active, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger:active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger:active .bp3-menu-item-label, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::before, .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active::after,
    .bp3-dark .bp3-menu-item.bp3-intent-danger.bp3-active .bp3-menu-item-label{
      color:#ffffff; }
  .bp3-dark .bp3-menu-item::before,
  .bp3-dark .bp3-menu-item > .bp3-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item .bp3-menu-item-label{
    color:#a7b6c2; }
  .bp3-dark .bp3-menu-item.bp3-active, .bp3-dark .bp3-menu-item:active{
    background-color:rgba(138, 155, 168, 0.3); }
  .bp3-dark .bp3-menu-item.bp3-disabled{
    color:rgba(167, 182, 194, 0.6) !important; }
    .bp3-dark .bp3-menu-item.bp3-disabled::before,
    .bp3-dark .bp3-menu-item.bp3-disabled > .bp3-icon,
    .bp3-dark .bp3-menu-item.bp3-disabled .bp3-menu-item-label{
      color:rgba(167, 182, 194, 0.6) !important; }

.bp3-dark .bp3-menu-divider,
.bp3-dark .bp3-menu-header{
  border-color:rgba(255, 255, 255, 0.15); }

.bp3-dark .bp3-menu-header > h6{
  color:#f5f8fa; }

.bp3-label .bp3-menu{
  margin-top:5px; }
.bp3-navbar{
  background-color:#ffffff;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.2);
  height:50px;
  padding:0 15px;
  position:relative;
  width:100%;
  z-index:10; }
  .bp3-navbar.bp3-dark,
  .bp3-dark .bp3-navbar{
    background-color:#394b59; }
  .bp3-navbar.bp3-dark{
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-dark .bp3-navbar{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 0 0 rgba(16, 22, 26, 0), 0 1px 1px rgba(16, 22, 26, 0.4); }
  .bp3-navbar.bp3-fixed-top{
    left:0;
    position:fixed;
    right:0;
    top:0; }

.bp3-navbar-heading{
  font-size:16px;
  margin-right:15px; }

.bp3-navbar-group{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:50px; }
  .bp3-navbar-group.bp3-align-left{
    float:left; }
  .bp3-navbar-group.bp3-align-right{
    float:right; }

.bp3-navbar-divider{
  border-left:1px solid rgba(16, 22, 26, 0.15);
  height:20px;
  margin:0 10px; }
  .bp3-dark .bp3-navbar-divider{
    border-left-color:rgba(255, 255, 255, 0.15); }
.bp3-non-ideal-state{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  height:100%;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  text-align:center;
  width:100%; }
  .bp3-non-ideal-state > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-non-ideal-state > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-non-ideal-state::before,
  .bp3-non-ideal-state > *{
    margin-bottom:20px; }
  .bp3-non-ideal-state:empty::before,
  .bp3-non-ideal-state > :last-child{
    margin-bottom:0; }
  .bp3-non-ideal-state > *{
    max-width:400px; }

.bp3-non-ideal-state-visual{
  color:rgba(92, 112, 128, 0.6);
  font-size:60px; }
  .bp3-dark .bp3-non-ideal-state-visual{
    color:rgba(167, 182, 194, 0.6); }

.bp3-overflow-list{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-wrap:nowrap;
      flex-wrap:nowrap;
  min-width:0; }

.bp3-overflow-list-spacer{
  -ms-flex-negative:1;
      flex-shrink:1;
  width:1px; }

body.bp3-overlay-open{
  overflow:hidden; }

.bp3-overlay{
  bottom:0;
  left:0;
  position:static;
  right:0;
  top:0;
  z-index:20; }
  .bp3-overlay:not(.bp3-overlay-open){
    pointer-events:none; }
  .bp3-overlay.bp3-overlay-container{
    overflow:hidden;
    position:fixed; }
    .bp3-overlay.bp3-overlay-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-scroll-container{
    overflow:auto;
    position:fixed; }
    .bp3-overlay.bp3-overlay-scroll-container.bp3-overlay-inline{
      position:absolute; }
  .bp3-overlay.bp3-overlay-inline{
    display:inline;
    overflow:visible; }

.bp3-overlay-content{
  position:fixed;
  z-index:20; }
  .bp3-overlay-inline .bp3-overlay-content,
  .bp3-overlay-scroll-container .bp3-overlay-content{
    position:absolute; }

.bp3-overlay-backdrop{
  bottom:0;
  left:0;
  position:fixed;
  right:0;
  top:0;
  opacity:1;
  background-color:rgba(16, 22, 26, 0.7);
  overflow:auto;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none;
  z-index:20; }
  .bp3-overlay-backdrop.bp3-overlay-enter, .bp3-overlay-backdrop.bp3-overlay-appear{
    opacity:0; }
  .bp3-overlay-backdrop.bp3-overlay-enter-active, .bp3-overlay-backdrop.bp3-overlay-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop.bp3-overlay-exit{
    opacity:1; }
  .bp3-overlay-backdrop.bp3-overlay-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-overlay-backdrop:focus{
    outline:none; }
  .bp3-overlay-inline .bp3-overlay-backdrop{
    position:absolute; }
.bp3-panel-stack{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack-view{
    background-color:#30404d; }
  .bp3-panel-stack-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack-push .bp3-panel-stack-enter, .bp3-panel-stack-push .bp3-panel-stack-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack-push .bp3-panel-stack-enter-active, .bp3-panel-stack-push .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-push .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-push .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-enter, .bp3-panel-stack-pop .bp3-panel-stack-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack-pop .bp3-panel-stack-enter-active, .bp3-panel-stack-pop .bp3-panel-stack-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack-pop .bp3-panel-stack-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack-pop .bp3-panel-stack-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-panel-stack2{
  overflow:hidden;
  position:relative; }

.bp3-panel-stack2-header{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  -webkit-box-shadow:0 1px rgba(16, 22, 26, 0.15);
          box-shadow:0 1px rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -ms-flex-negative:0;
      flex-shrink:0;
  height:30px;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-header{
    -webkit-box-shadow:0 1px rgba(255, 255, 255, 0.15);
            box-shadow:0 1px rgba(255, 255, 255, 0.15); }
  .bp3-panel-stack2-header > span{
    -webkit-box-align:stretch;
        -ms-flex-align:stretch;
            align-items:stretch;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-flex:1;
        -ms-flex:1;
            flex:1; }
  .bp3-panel-stack2-header .bp3-heading{
    margin:0 5px; }

.bp3-button.bp3-panel-stack2-header-back{
  margin-left:5px;
  padding-left:0;
  white-space:nowrap; }
  .bp3-button.bp3-panel-stack2-header-back .bp3-icon{
    margin:0 2px; }

.bp3-panel-stack2-view{
  bottom:0;
  left:0;
  position:absolute;
  right:0;
  top:0;
  background-color:#ffffff;
  border-right:1px solid rgba(16, 22, 26, 0.15);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  margin-right:-1px;
  overflow-y:auto;
  z-index:1; }
  .bp3-dark .bp3-panel-stack2-view{
    background-color:#30404d; }
  .bp3-panel-stack2-view:nth-last-child(n + 4){
    display:none; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter, .bp3-panel-stack2-push .bp3-panel-stack2-appear{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0; }

.bp3-panel-stack2-push .bp3-panel-stack2-enter-active, .bp3-panel-stack2-push .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-push .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter, .bp3-panel-stack2-pop .bp3-panel-stack2-appear{
  -webkit-transform:translateX(-50%);
          transform:translateX(-50%);
  opacity:0; }

.bp3-panel-stack2-pop .bp3-panel-stack2-enter-active, .bp3-panel-stack2-pop .bp3-panel-stack2-appear-active{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit{
  -webkit-transform:translate(0%);
          transform:translate(0%);
  opacity:1; }

.bp3-panel-stack2-pop .bp3-panel-stack2-exit-active{
  -webkit-transform:translateX(100%);
          transform:translateX(100%);
  opacity:0;
  -webkit-transition-delay:0;
          transition-delay:0;
  -webkit-transition-duration:400ms;
          transition-duration:400ms;
  -webkit-transition-property:opacity, -webkit-transform;
  transition-property:opacity, -webkit-transform;
  transition-property:transform, opacity;
  transition-property:transform, opacity, -webkit-transform;
  -webkit-transition-timing-function:ease;
          transition-timing-function:ease; }
.bp3-popover{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1);
  border-radius:3px;
  display:inline-block;
  z-index:20; }
  .bp3-popover .bp3-popover-arrow{
    height:30px;
    position:absolute;
    width:30px; }
    .bp3-popover .bp3-popover-arrow::before{
      height:20px;
      margin:5px;
      width:20px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover{
    margin-bottom:17px;
    margin-top:-17px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
      bottom:-11px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover{
    margin-left:17px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
      left:-11px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover{
    margin-top:17px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
      top:-11px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover{
    margin-left:-17px;
    margin-right:17px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
      right:-11px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-popover > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-popover > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-popover > .bp3-popover-arrow{
    top:-0.3934px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-popover > .bp3-popover-arrow{
    right:-0.3934px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-popover > .bp3-popover-arrow{
    left:-0.3934px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-popover > .bp3-popover-arrow{
    bottom:-0.3934px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-popover{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-popover{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-popover{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-popover .bp3-popover-content{
    background:#ffffff;
    color:inherit; }
  .bp3-popover .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-popover .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-popover .bp3-popover-arrow-fill{
    fill:#ffffff; }
  .bp3-popover-enter > .bp3-popover, .bp3-popover-appear > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3); }
  .bp3-popover-enter-active > .bp3-popover, .bp3-popover-appear-active > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover-exit > .bp3-popover{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-popover{
    -webkit-transform:scale(0.3);
            transform:scale(0.3);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-popover .bp3-popover-content{
    border-radius:3px;
    position:relative; }
  .bp3-popover.bp3-popover-content-sizing .bp3-popover-content{
    max-width:350px;
    padding:20px; }
  .bp3-popover-target + .bp3-overlay .bp3-popover.bp3-popover-content-sizing{
    width:350px; }
  .bp3-popover.bp3-minimal{
    margin:0 !important; }
    .bp3-popover.bp3-minimal .bp3-popover-arrow{
      display:none; }
    .bp3-popover.bp3-minimal.bp3-popover{
      -webkit-transform:scale(1);
              transform:scale(1); }
      .bp3-popover-enter > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-enter-active > .bp3-popover.bp3-minimal.bp3-popover, .bp3-popover-appear-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
      .bp3-popover-exit > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1); }
      .bp3-popover-exit-active > .bp3-popover.bp3-minimal.bp3-popover{
        -webkit-transform:scale(1);
                transform:scale(1);
        -webkit-transition-delay:0;
                transition-delay:0;
        -webkit-transition-duration:100ms;
                transition-duration:100ms;
        -webkit-transition-property:-webkit-transform;
        transition-property:-webkit-transform;
        transition-property:transform;
        transition-property:transform, -webkit-transform;
        -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
                transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover.bp3-dark,
  .bp3-dark .bp3-popover{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-popover .bp3-popover-content{
      background:#30404d;
      color:inherit; }
    .bp3-popover.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-popover .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-popover.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-popover .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-popover.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-popover .bp3-popover-arrow-fill{
      fill:#30404d; }

.bp3-popover-arrow::before{
  border-radius:2px;
  content:"";
  display:block;
  position:absolute;
  -webkit-transform:rotate(45deg);
          transform:rotate(45deg); }

.bp3-tether-pinned .bp3-popover-arrow{
  display:none; }

.bp3-popover-backdrop{
  background:rgba(255, 255, 255, 0); }

.bp3-transition-container{
  opacity:1;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  z-index:20; }
  .bp3-transition-container.bp3-popover-enter, .bp3-transition-container.bp3-popover-appear{
    opacity:0; }
  .bp3-transition-container.bp3-popover-enter-active, .bp3-transition-container.bp3-popover-appear-active{
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container.bp3-popover-exit{
    opacity:1; }
  .bp3-transition-container.bp3-popover-exit-active{
    opacity:0;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:opacity;
    transition-property:opacity;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-transition-container:focus{
    outline:none; }
  .bp3-transition-container.bp3-popover-leave .bp3-popover-content{
    pointer-events:none; }
  .bp3-transition-container[data-x-out-of-boundaries]{
    display:none; }

span.bp3-popover-target{
  display:inline-block; }

.bp3-popover-wrapper.bp3-fill{
  width:100%; }

.bp3-portal{
  left:0;
  position:absolute;
  right:0;
  top:0; }
@-webkit-keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }
@keyframes linear-progress-bar-stripes{
  from{
    background-position:0 0; }
  to{
    background-position:30px 0; } }

.bp3-progress-bar{
  background:rgba(92, 112, 128, 0.2);
  border-radius:40px;
  display:block;
  height:8px;
  overflow:hidden;
  position:relative;
  width:100%; }
  .bp3-progress-bar .bp3-progress-meter{
    background:linear-gradient(-45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%);
    background-color:rgba(92, 112, 128, 0.8);
    background-size:30px 30px;
    border-radius:40px;
    height:100%;
    position:absolute;
    -webkit-transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:width 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    width:100%; }
  .bp3-progress-bar:not(.bp3-no-animation):not(.bp3-no-stripes) .bp3-progress-meter{
    animation:linear-progress-bar-stripes 300ms linear infinite reverse; }
  .bp3-progress-bar.bp3-no-stripes .bp3-progress-meter{
    background-image:none; }

.bp3-dark .bp3-progress-bar{
  background:rgba(16, 22, 26, 0.5); }
  .bp3-dark .bp3-progress-bar .bp3-progress-meter{
    background-color:#8a9ba8; }

.bp3-progress-bar.bp3-intent-primary .bp3-progress-meter{
  background-color:#137cbd; }

.bp3-progress-bar.bp3-intent-success .bp3-progress-meter{
  background-color:#0f9960; }

.bp3-progress-bar.bp3-intent-warning .bp3-progress-meter{
  background-color:#d9822b; }

.bp3-progress-bar.bp3-intent-danger .bp3-progress-meter{
  background-color:#db3737; }
@-webkit-keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
@keyframes skeleton-glow{
  from{
    background:rgba(206, 217, 224, 0.2);
    border-color:rgba(206, 217, 224, 0.2); }
  to{
    background:rgba(92, 112, 128, 0.2);
    border-color:rgba(92, 112, 128, 0.2); } }
.bp3-skeleton{
  -webkit-animation:1000ms linear infinite alternate skeleton-glow;
          animation:1000ms linear infinite alternate skeleton-glow;
  background:rgba(206, 217, 224, 0.2);
  background-clip:padding-box !important;
  border-color:rgba(206, 217, 224, 0.2) !important;
  border-radius:2px;
  -webkit-box-shadow:none !important;
          box-shadow:none !important;
  color:transparent !important;
  cursor:default;
  pointer-events:none;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-skeleton::before, .bp3-skeleton::after,
  .bp3-skeleton *{
    visibility:hidden !important; }
.bp3-slider{
  height:40px;
  min-width:150px;
  width:100%;
  cursor:default;
  outline:none;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-slider:hover{
    cursor:pointer; }
  .bp3-slider:active{
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-slider.bp3-disabled{
    cursor:not-allowed;
    opacity:0.5; }
  .bp3-slider.bp3-slider-unlabeled{
    height:16px; }

.bp3-slider-track,
.bp3-slider-progress{
  height:6px;
  left:0;
  right:0;
  top:5px;
  position:absolute; }

.bp3-slider-track{
  border-radius:3px;
  overflow:hidden; }

.bp3-slider-progress{
  background:rgba(92, 112, 128, 0.2); }
  .bp3-dark .bp3-slider-progress{
    background:rgba(16, 22, 26, 0.5); }
  .bp3-slider-progress.bp3-intent-primary{
    background-color:#137cbd; }
  .bp3-slider-progress.bp3-intent-success{
    background-color:#0f9960; }
  .bp3-slider-progress.bp3-intent-warning{
    background-color:#d9822b; }
  .bp3-slider-progress.bp3-intent-danger{
    background-color:#db3737; }

.bp3-slider-handle{
  background-color:#f5f8fa;
  background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.8)), to(rgba(255, 255, 255, 0)));
  background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.8), rgba(255, 255, 255, 0));
  -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
          box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
  color:#182026;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
  cursor:pointer;
  height:16px;
  left:0;
  position:absolute;
  top:0;
  width:16px; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1); }
  .bp3-slider-handle:active, .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
  .bp3-slider-handle:disabled, .bp3-slider-handle.bp3-disabled{
    background-color:rgba(206, 217, 224, 0.5);
    background-image:none;
    -webkit-box-shadow:none;
            box-shadow:none;
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed;
    outline:none; }
    .bp3-slider-handle:disabled.bp3-active, .bp3-slider-handle:disabled.bp3-active:hover, .bp3-slider-handle.bp3-disabled.bp3-active, .bp3-slider-handle.bp3-disabled.bp3-active:hover{
      background:rgba(206, 217, 224, 0.7); }
  .bp3-slider-handle:focus{
    z-index:1; }
  .bp3-slider-handle:hover{
    background-clip:padding-box;
    background-color:#ebf1f5;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 -1px 0 rgba(16, 22, 26, 0.1);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 1px 1px rgba(16, 22, 26, 0.2);
    cursor:-webkit-grab;
    cursor:grab;
    z-index:2; }
  .bp3-slider-handle.bp3-active{
    background-color:#d8e1e8;
    background-image:none;
    -webkit-box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
            box-shadow:inset 0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 2px rgba(16, 22, 26, 0.2);
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), inset 0 1px 1px rgba(16, 22, 26, 0.1);
    cursor:-webkit-grabbing;
    cursor:grabbing; }
  .bp3-disabled .bp3-slider-handle{
    background:#bfccd6;
    -webkit-box-shadow:none;
            box-shadow:none;
    pointer-events:none; }
  .bp3-dark .bp3-slider-handle{
    background-color:#394b59;
    background-image:-webkit-gradient(linear, left top, left bottom, from(rgba(255, 255, 255, 0.05)), to(rgba(255, 255, 255, 0)));
    background-image:linear-gradient(to bottom, rgba(255, 255, 255, 0.05), rgba(255, 255, 255, 0));
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
    color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover, .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      color:#f5f8fa; }
    .bp3-dark .bp3-slider-handle:hover{
      background-color:#30404d;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-slider-handle:active, .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#202b33;
      background-image:none;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.6), inset 0 1px 2px rgba(16, 22, 26, 0.2); }
    .bp3-dark .bp3-slider-handle:disabled, .bp3-dark .bp3-slider-handle.bp3-disabled{
      background-color:rgba(57, 75, 89, 0.5);
      background-image:none;
      -webkit-box-shadow:none;
              box-shadow:none;
      color:rgba(167, 182, 194, 0.6); }
      .bp3-dark .bp3-slider-handle:disabled.bp3-active, .bp3-dark .bp3-slider-handle.bp3-disabled.bp3-active{
        background:rgba(57, 75, 89, 0.7); }
    .bp3-dark .bp3-slider-handle .bp3-button-spinner .bp3-spinner-head{
      background:rgba(16, 22, 26, 0.5);
      stroke:#8a9ba8; }
    .bp3-dark .bp3-slider-handle, .bp3-dark .bp3-slider-handle:hover{
      background-color:#394b59; }
    .bp3-dark .bp3-slider-handle.bp3-active{
      background-color:#293742; }
  .bp3-dark .bp3-disabled .bp3-slider-handle{
    background:#5c7080;
    border-color:#5c7080;
    -webkit-box-shadow:none;
            box-shadow:none; }
  .bp3-slider-handle .bp3-slider-label{
    background:#394b59;
    border-radius:3px;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
    color:#f5f8fa;
    margin-left:8px; }
    .bp3-dark .bp3-slider-handle .bp3-slider-label{
      background:#e1e8ed;
      -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
      color:#394b59; }
    .bp3-disabled .bp3-slider-handle .bp3-slider-label{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-slider-handle.bp3-start, .bp3-slider-handle.bp3-end{
    width:8px; }
  .bp3-slider-handle.bp3-start{
    border-bottom-right-radius:0;
    border-top-right-radius:0; }
  .bp3-slider-handle.bp3-end{
    border-bottom-left-radius:0;
    border-top-left-radius:0;
    margin-left:8px; }
    .bp3-slider-handle.bp3-end .bp3-slider-label{
      margin-left:0; }

.bp3-slider-label{
  -webkit-transform:translate(-50%, 20px);
          transform:translate(-50%, 20px);
  display:inline-block;
  font-size:12px;
  line-height:1;
  padding:2px 5px;
  position:absolute;
  vertical-align:top; }

.bp3-slider.bp3-vertical{
  height:150px;
  min-width:40px;
  width:40px; }
  .bp3-slider.bp3-vertical .bp3-slider-track,
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    bottom:0;
    height:auto;
    left:5px;
    top:0;
    width:6px; }
  .bp3-slider.bp3-vertical .bp3-slider-progress{
    top:auto; }
  .bp3-slider.bp3-vertical .bp3-slider-label{
    -webkit-transform:translate(20px, 50%);
            transform:translate(20px, 50%); }
  .bp3-slider.bp3-vertical .bp3-slider-handle{
    top:auto; }
    .bp3-slider.bp3-vertical .bp3-slider-handle .bp3-slider-label{
      margin-left:0;
      margin-top:-8px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end, .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      height:8px;
      margin-left:0;
      width:16px; }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start{
      border-bottom-right-radius:3px;
      border-top-left-radius:0; }
      .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-start .bp3-slider-label{
        -webkit-transform:translate(20px);
                transform:translate(20px); }
    .bp3-slider.bp3-vertical .bp3-slider-handle.bp3-end{
      border-bottom-left-radius:0;
      border-bottom-right-radius:0;
      border-top-left-radius:3px;
      margin-bottom:8px; }

@-webkit-keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

@keyframes pt-spinner-animation{
  from{
    -webkit-transform:rotate(0deg);
            transform:rotate(0deg); }
  to{
    -webkit-transform:rotate(360deg);
            transform:rotate(360deg); } }

.bp3-spinner{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-pack:center;
      -ms-flex-pack:center;
          justify-content:center;
  overflow:visible;
  vertical-align:middle; }
  .bp3-spinner svg{
    display:block; }
  .bp3-spinner path{
    fill-opacity:0; }
  .bp3-spinner .bp3-spinner-head{
    stroke:rgba(92, 112, 128, 0.8);
    stroke-linecap:round;
    -webkit-transform-origin:center;
            transform-origin:center;
    -webkit-transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
    transition:stroke-dashoffset 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-spinner .bp3-spinner-track{
    stroke:rgba(92, 112, 128, 0.2); }

.bp3-spinner-animation{
  -webkit-animation:pt-spinner-animation 500ms linear infinite;
          animation:pt-spinner-animation 500ms linear infinite; }
  .bp3-no-spin > .bp3-spinner-animation{
    -webkit-animation:none;
            animation:none; }

.bp3-dark .bp3-spinner .bp3-spinner-head{
  stroke:#8a9ba8; }

.bp3-dark .bp3-spinner .bp3-spinner-track{
  stroke:rgba(16, 22, 26, 0.5); }

.bp3-spinner.bp3-intent-primary .bp3-spinner-head{
  stroke:#137cbd; }

.bp3-spinner.bp3-intent-success .bp3-spinner-head{
  stroke:#0f9960; }

.bp3-spinner.bp3-intent-warning .bp3-spinner-head{
  stroke:#d9822b; }

.bp3-spinner.bp3-intent-danger .bp3-spinner-head{
  stroke:#db3737; }
.bp3-tabs.bp3-vertical{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex; }
  .bp3-tabs.bp3-vertical > .bp3-tab-list{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start;
    -webkit-box-orient:vertical;
    -webkit-box-direction:normal;
        -ms-flex-direction:column;
            flex-direction:column; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab{
      border-radius:3px;
      padding:0 10px;
      width:100%; }
      .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab[aria-selected="true"]{
        background-color:rgba(19, 124, 189, 0.2);
        -webkit-box-shadow:none;
                box-shadow:none; }
    .bp3-tabs.bp3-vertical > .bp3-tab-list .bp3-tab-indicator-wrapper .bp3-tab-indicator{
      background-color:rgba(19, 124, 189, 0.2);
      border-radius:3px;
      bottom:0;
      height:auto;
      left:0;
      right:0;
      top:0; }
  .bp3-tabs.bp3-vertical > .bp3-tab-panel{
    margin-top:0;
    padding-left:20px; }

.bp3-tab-list{
  -webkit-box-align:end;
      -ms-flex-align:end;
          align-items:flex-end;
  border:none;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  list-style:none;
  margin:0;
  padding:0;
  position:relative; }
  .bp3-tab-list > *:not(:last-child){
    margin-right:20px; }

.bp3-tab{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  color:#182026;
  cursor:pointer;
  -webkit-box-flex:0;
      -ms-flex:0 0 auto;
          flex:0 0 auto;
  font-size:14px;
  line-height:30px;
  max-width:100%;
  position:relative;
  vertical-align:top; }
  .bp3-tab a{
    color:inherit;
    display:block;
    text-decoration:none; }
  .bp3-tab-indicator-wrapper ~ .bp3-tab{
    background-color:transparent !important;
    -webkit-box-shadow:none !important;
            box-shadow:none !important; }
  .bp3-tab[aria-disabled="true"]{
    color:rgba(92, 112, 128, 0.6);
    cursor:not-allowed; }
  .bp3-tab[aria-selected="true"]{
    border-radius:0;
    -webkit-box-shadow:inset 0 -3px 0 #106ba3;
            box-shadow:inset 0 -3px 0 #106ba3; }
  .bp3-tab[aria-selected="true"], .bp3-tab:not([aria-disabled="true"]):hover{
    color:#106ba3; }
  .bp3-tab:focus{
    -moz-outline-radius:0; }
  .bp3-large > .bp3-tab{
    font-size:16px;
    line-height:40px; }

.bp3-tab-panel{
  margin-top:20px; }
  .bp3-tab-panel[aria-hidden="true"]{
    display:none; }

.bp3-tab-indicator-wrapper{
  left:0;
  pointer-events:none;
  position:absolute;
  top:0;
  -webkit-transform:translateX(0), translateY(0);
          transform:translateX(0), translateY(0);
  -webkit-transition:height, width, -webkit-transform;
  transition:height, width, -webkit-transform;
  transition:height, transform, width;
  transition:height, transform, width, -webkit-transform;
  -webkit-transition-duration:200ms;
          transition-duration:200ms;
  -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
          transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tab-indicator-wrapper .bp3-tab-indicator{
    background-color:#106ba3;
    bottom:0;
    height:3px;
    left:0;
    position:absolute;
    right:0; }
  .bp3-tab-indicator-wrapper.bp3-no-animation{
    -webkit-transition:none;
    transition:none; }

.bp3-dark .bp3-tab{
  color:#f5f8fa; }
  .bp3-dark .bp3-tab[aria-disabled="true"]{
    color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tab[aria-selected="true"]{
    -webkit-box-shadow:inset 0 -3px 0 #48aff0;
            box-shadow:inset 0 -3px 0 #48aff0; }
  .bp3-dark .bp3-tab[aria-selected="true"], .bp3-dark .bp3-tab:not([aria-disabled="true"]):hover{
    color:#48aff0; }

.bp3-dark .bp3-tab-indicator{
  background-color:#48aff0; }

.bp3-flex-expander{
  -webkit-box-flex:1;
      -ms-flex:1 1;
          flex:1 1; }
.bp3-tag{
  display:-webkit-inline-box;
  display:-ms-inline-flexbox;
  display:inline-flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  background-color:#5c7080;
  border:none;
  border-radius:3px;
  -webkit-box-shadow:none;
          box-shadow:none;
  color:#f5f8fa;
  font-size:12px;
  line-height:16px;
  max-width:100%;
  min-height:20px;
  min-width:20px;
  padding:2px 6px;
  position:relative; }
  .bp3-tag.bp3-interactive{
    cursor:pointer; }
    .bp3-tag.bp3-interactive:hover{
      background-color:rgba(92, 112, 128, 0.85); }
    .bp3-tag.bp3-interactive.bp3-active, .bp3-tag.bp3-interactive:active{
      background-color:rgba(92, 112, 128, 0.7); }
  .bp3-tag > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag > .bp3-fill{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag::before,
  .bp3-tag > *{
    margin-right:4px; }
  .bp3-tag:empty::before,
  .bp3-tag > :last-child{
    margin-right:0; }
  .bp3-tag:focus{
    outline:rgba(19, 124, 189, 0.6) auto 2px;
    outline-offset:0;
    -moz-outline-radius:6px; }
  .bp3-tag.bp3-round{
    border-radius:30px;
    padding-left:8px;
    padding-right:8px; }
  .bp3-dark .bp3-tag{
    background-color:#bfccd6;
    color:#182026; }
    .bp3-dark .bp3-tag.bp3-interactive{
      cursor:pointer; }
      .bp3-dark .bp3-tag.bp3-interactive:hover{
        background-color:rgba(191, 204, 214, 0.85); }
      .bp3-dark .bp3-tag.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-interactive:active{
        background-color:rgba(191, 204, 214, 0.7); }
    .bp3-dark .bp3-tag > .bp3-icon, .bp3-dark .bp3-tag .bp3-icon-standard, .bp3-dark .bp3-tag .bp3-icon-large{
      fill:currentColor; }
  .bp3-tag > .bp3-icon, .bp3-tag .bp3-icon-standard, .bp3-tag .bp3-icon-large{
    fill:#ffffff; }
  .bp3-tag.bp3-large,
  .bp3-large .bp3-tag{
    font-size:14px;
    line-height:20px;
    min-height:30px;
    min-width:30px;
    padding:5px 10px; }
    .bp3-tag.bp3-large::before,
    .bp3-tag.bp3-large > *,
    .bp3-large .bp3-tag::before,
    .bp3-large .bp3-tag > *{
      margin-right:7px; }
    .bp3-tag.bp3-large:empty::before,
    .bp3-tag.bp3-large > :last-child,
    .bp3-large .bp3-tag:empty::before,
    .bp3-large .bp3-tag > :last-child{
      margin-right:0; }
    .bp3-tag.bp3-large.bp3-round,
    .bp3-large .bp3-tag.bp3-round{
      padding-left:12px;
      padding-right:12px; }
  .bp3-tag.bp3-intent-primary{
    background:#137cbd;
    color:#ffffff; }
    .bp3-tag.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.85); }
      .bp3-tag.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.7); }
  .bp3-tag.bp3-intent-success{
    background:#0f9960;
    color:#ffffff; }
    .bp3-tag.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.85); }
      .bp3-tag.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.7); }
  .bp3-tag.bp3-intent-warning{
    background:#d9822b;
    color:#ffffff; }
    .bp3-tag.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.85); }
      .bp3-tag.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.7); }
  .bp3-tag.bp3-intent-danger{
    background:#db3737;
    color:#ffffff; }
    .bp3-tag.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.85); }
      .bp3-tag.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.7); }
  .bp3-tag.bp3-fill{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    width:100%; }
  .bp3-tag.bp3-minimal > .bp3-icon, .bp3-tag.bp3-minimal .bp3-icon-standard, .bp3-tag.bp3-minimal .bp3-icon-large{
    fill:#5c7080; }
  .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
    background-color:rgba(138, 155, 168, 0.2);
    color:#182026; }
    .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
        background-color:rgba(92, 112, 128, 0.3); }
      .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
        background-color:rgba(92, 112, 128, 0.4); }
    .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]){
      color:#f5f8fa; }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:hover{
          background-color:rgba(191, 204, 214, 0.3); }
        .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]).bp3-interactive:active{
          background-color:rgba(191, 204, 214, 0.4); }
      .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) > .bp3-icon, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-standard, .bp3-dark .bp3-tag.bp3-minimal:not([class*="bp3-intent-"]) .bp3-icon-large{
        fill:#a7b6c2; }
  .bp3-tag.bp3-minimal.bp3-intent-primary{
    background-color:rgba(19, 124, 189, 0.15);
    color:#106ba3; }
    .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
        background-color:rgba(19, 124, 189, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
        background-color:rgba(19, 124, 189, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-primary > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-primary .bp3-icon-large{
      fill:#137cbd; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary{
      background-color:rgba(19, 124, 189, 0.25);
      color:#48aff0; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:hover{
          background-color:rgba(19, 124, 189, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-primary.bp3-interactive:active{
          background-color:rgba(19, 124, 189, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-success{
    background-color:rgba(15, 153, 96, 0.15);
    color:#0d8050; }
    .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
        background-color:rgba(15, 153, 96, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
        background-color:rgba(15, 153, 96, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-success > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-success .bp3-icon-large{
      fill:#0f9960; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success{
      background-color:rgba(15, 153, 96, 0.25);
      color:#3dcc91; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:hover{
          background-color:rgba(15, 153, 96, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-success.bp3-interactive:active{
          background-color:rgba(15, 153, 96, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-warning{
    background-color:rgba(217, 130, 43, 0.15);
    color:#bf7326; }
    .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
        background-color:rgba(217, 130, 43, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
        background-color:rgba(217, 130, 43, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-warning > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-warning .bp3-icon-large{
      fill:#d9822b; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning{
      background-color:rgba(217, 130, 43, 0.25);
      color:#ffb366; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:hover{
          background-color:rgba(217, 130, 43, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-warning.bp3-interactive:active{
          background-color:rgba(217, 130, 43, 0.45); }
  .bp3-tag.bp3-minimal.bp3-intent-danger{
    background-color:rgba(219, 55, 55, 0.15);
    color:#c23030; }
    .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
      cursor:pointer; }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
        background-color:rgba(219, 55, 55, 0.25); }
      .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
        background-color:rgba(219, 55, 55, 0.35); }
    .bp3-tag.bp3-minimal.bp3-intent-danger > .bp3-icon, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-standard, .bp3-tag.bp3-minimal.bp3-intent-danger .bp3-icon-large{
      fill:#db3737; }
    .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger{
      background-color:rgba(219, 55, 55, 0.25);
      color:#ff7373; }
      .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive{
        cursor:pointer; }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:hover{
          background-color:rgba(219, 55, 55, 0.35); }
        .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive.bp3-active, .bp3-dark .bp3-tag.bp3-minimal.bp3-intent-danger.bp3-interactive:active{
          background-color:rgba(219, 55, 55, 0.45); }

.bp3-tag-remove{
  background:none;
  border:none;
  color:inherit;
  cursor:pointer;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin-bottom:-2px;
  margin-right:-6px !important;
  margin-top:-2px;
  opacity:0.5;
  padding:2px;
  padding-left:0; }
  .bp3-tag-remove:hover{
    background:none;
    opacity:0.8;
    text-decoration:none; }
  .bp3-tag-remove:active{
    opacity:1; }
  .bp3-tag-remove:empty::before{
    font-family:"Icons16", sans-serif;
    font-size:16px;
    font-style:normal;
    font-weight:400;
    line-height:1;
    -moz-osx-font-smoothing:grayscale;
    -webkit-font-smoothing:antialiased;
    content:""; }
  .bp3-large .bp3-tag-remove{
    margin-right:-10px !important;
    padding:0 5px 0 0; }
    .bp3-large .bp3-tag-remove:empty::before{
      font-family:"Icons20", sans-serif;
      font-size:20px;
      font-style:normal;
      font-weight:400;
      line-height:1; }
.bp3-tag-input{
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  -webkit-box-orient:horizontal;
  -webkit-box-direction:normal;
      -ms-flex-direction:row;
          flex-direction:row;
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  cursor:text;
  height:auto;
  line-height:inherit;
  min-height:30px;
  padding-left:5px;
  padding-right:0; }
  .bp3-tag-input > *{
    -webkit-box-flex:0;
        -ms-flex-positive:0;
            flex-grow:0;
    -ms-flex-negative:0;
        flex-shrink:0; }
  .bp3-tag-input > .bp3-tag-input-values{
    -webkit-box-flex:1;
        -ms-flex-positive:1;
            flex-grow:1;
    -ms-flex-negative:1;
        flex-shrink:1; }
  .bp3-tag-input .bp3-tag-input-icon{
    color:#5c7080;
    margin-left:2px;
    margin-right:7px;
    margin-top:7px; }
  .bp3-tag-input .bp3-tag-input-values{
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex;
    -webkit-box-orient:horizontal;
    -webkit-box-direction:normal;
        -ms-flex-direction:row;
            flex-direction:row;
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    -ms-flex-item-align:stretch;
        align-self:stretch;
    -ms-flex-wrap:wrap;
        flex-wrap:wrap;
    margin-right:7px;
    margin-top:5px;
    min-width:0; }
    .bp3-tag-input .bp3-tag-input-values > *{
      -webkit-box-flex:0;
          -ms-flex-positive:0;
              flex-grow:0;
      -ms-flex-negative:0;
          flex-shrink:0; }
    .bp3-tag-input .bp3-tag-input-values > .bp3-fill{
      -webkit-box-flex:1;
          -ms-flex-positive:1;
              flex-grow:1;
      -ms-flex-negative:1;
          flex-shrink:1; }
    .bp3-tag-input .bp3-tag-input-values::before,
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-right:5px; }
    .bp3-tag-input .bp3-tag-input-values:empty::before,
    .bp3-tag-input .bp3-tag-input-values > :last-child{
      margin-right:0; }
    .bp3-tag-input .bp3-tag-input-values:first-child .bp3-input-ghost:first-child{
      padding-left:5px; }
    .bp3-tag-input .bp3-tag-input-values > *{
      margin-bottom:5px; }
  .bp3-tag-input .bp3-tag{
    overflow-wrap:break-word; }
    .bp3-tag-input .bp3-tag.bp3-active{
      outline:rgba(19, 124, 189, 0.6) auto 2px;
      outline-offset:0;
      -moz-outline-radius:6px; }
  .bp3-tag-input .bp3-input-ghost{
    -webkit-box-flex:1;
        -ms-flex:1 1 auto;
            flex:1 1 auto;
    line-height:20px;
    width:80px; }
    .bp3-tag-input .bp3-input-ghost:disabled, .bp3-tag-input .bp3-input-ghost.bp3-disabled{
      cursor:not-allowed; }
  .bp3-tag-input .bp3-button,
  .bp3-tag-input .bp3-spinner{
    margin:3px;
    margin-left:0; }
  .bp3-tag-input .bp3-button{
    min-height:24px;
    min-width:24px;
    padding:0 7px; }
  .bp3-tag-input.bp3-large{
    height:auto;
    min-height:40px; }
    .bp3-tag-input.bp3-large::before,
    .bp3-tag-input.bp3-large > *{
      margin-right:10px; }
    .bp3-tag-input.bp3-large:empty::before,
    .bp3-tag-input.bp3-large > :last-child{
      margin-right:0; }
    .bp3-tag-input.bp3-large .bp3-tag-input-icon{
      margin-left:5px;
      margin-top:10px; }
    .bp3-tag-input.bp3-large .bp3-input-ghost{
      line-height:30px; }
    .bp3-tag-input.bp3-large .bp3-button{
      min-height:30px;
      min-width:30px;
      padding:5px 10px;
      margin:5px;
      margin-left:0; }
    .bp3-tag-input.bp3-large .bp3-spinner{
      margin:8px;
      margin-left:0; }
  .bp3-tag-input.bp3-active{
    background-color:#ffffff;
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
    .bp3-tag-input.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.2); }
  .bp3-dark .bp3-tag-input .bp3-tag-input-icon, .bp3-tag-input.bp3-dark .bp3-tag-input-icon{
    color:#a7b6c2; }
  .bp3-dark .bp3-tag-input .bp3-input-ghost, .bp3-tag-input.bp3-dark .bp3-input-ghost{
    color:#f5f8fa; }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-webkit-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-webkit-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-moz-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-moz-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost:-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost:-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::-ms-input-placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::-ms-input-placeholder{
      color:rgba(167, 182, 194, 0.6); }
    .bp3-dark .bp3-tag-input .bp3-input-ghost::placeholder, .bp3-tag-input.bp3-dark .bp3-input-ghost::placeholder{
      color:rgba(167, 182, 194, 0.6); }
  .bp3-dark .bp3-tag-input.bp3-active, .bp3-tag-input.bp3-dark.bp3-active{
    background-color:rgba(16, 22, 26, 0.3);
    -webkit-box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px #137cbd, 0 0 0 1px #137cbd, 0 0 0 3px rgba(19, 124, 189, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-primary, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-primary{
      -webkit-box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #106ba3, 0 0 0 3px rgba(16, 107, 163, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-success, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-success{
      -webkit-box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #0d8050, 0 0 0 3px rgba(13, 128, 80, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-warning, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-warning{
      -webkit-box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #bf7326, 0 0 0 3px rgba(191, 115, 38, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }
    .bp3-dark .bp3-tag-input.bp3-active.bp3-intent-danger, .bp3-tag-input.bp3-dark.bp3-active.bp3-intent-danger{
      -webkit-box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4);
              box-shadow:0 0 0 1px #c23030, 0 0 0 3px rgba(194, 48, 48, 0.3), inset 0 0 0 1px rgba(16, 22, 26, 0.3), inset 0 1px 1px rgba(16, 22, 26, 0.4); }

.bp3-input-ghost{
  background:none;
  border:none;
  -webkit-box-shadow:none;
          box-shadow:none;
  padding:0; }
  .bp3-input-ghost::-webkit-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-moz-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::-ms-input-placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost::placeholder{
    color:rgba(92, 112, 128, 0.6);
    opacity:1; }
  .bp3-input-ghost:focus{
    outline:none !important; }
.bp3-toast{
  -webkit-box-align:start;
      -ms-flex-align:start;
          align-items:flex-start;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  margin:20px 0 0;
  max-width:500px;
  min-width:300px;
  pointer-events:all;
  position:relative !important; }
  .bp3-toast.bp3-toast-enter, .bp3-toast.bp3-toast-appear{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active, .bp3-toast.bp3-toast-appear-active{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-enter ~ .bp3-toast, .bp3-toast.bp3-toast-appear ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px); }
  .bp3-toast.bp3-toast-enter-active ~ .bp3-toast, .bp3-toast.bp3-toast-appear-active ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11);
            transition-timing-function:cubic-bezier(0.54, 1.12, 0.38, 1.11); }
  .bp3-toast.bp3-toast-exit{
    opacity:1;
    -webkit-filter:blur(0);
            filter:blur(0); }
  .bp3-toast.bp3-toast-exit-active{
    opacity:0;
    -webkit-filter:blur(10px);
            filter:blur(10px);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:300ms;
            transition-duration:300ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:opacity, filter;
    transition-property:opacity, filter, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast.bp3-toast-exit ~ .bp3-toast{
    -webkit-transform:translateY(0);
            transform:translateY(0); }
  .bp3-toast.bp3-toast-exit-active ~ .bp3-toast{
    -webkit-transform:translateY(-40px);
            transform:translateY(-40px);
    -webkit-transition-delay:50ms;
            transition-delay:50ms;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-toast .bp3-button-group{
    -webkit-box-flex:0;
        -ms-flex:0 0 auto;
            flex:0 0 auto;
    padding:5px;
    padding-left:0; }
  .bp3-toast > .bp3-icon{
    color:#5c7080;
    margin:12px;
    margin-right:0; }
  .bp3-toast.bp3-dark,
  .bp3-dark .bp3-toast{
    background-color:#394b59;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-toast.bp3-dark > .bp3-icon,
    .bp3-dark .bp3-toast > .bp3-icon{
      color:#a7b6c2; }
  .bp3-toast[class*="bp3-intent-"] a{
    color:rgba(255, 255, 255, 0.7); }
    .bp3-toast[class*="bp3-intent-"] a:hover{
      color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] > .bp3-icon{
    color:#ffffff; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button, .bp3-toast[class*="bp3-intent-"] .bp3-button::before,
  .bp3-toast[class*="bp3-intent-"] .bp3-button .bp3-icon, .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    color:rgba(255, 255, 255, 0.7) !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:focus{
    outline-color:rgba(255, 255, 255, 0.5); }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:hover{
    background-color:rgba(255, 255, 255, 0.15) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button:active{
    background-color:rgba(255, 255, 255, 0.3) !important;
    color:#ffffff !important; }
  .bp3-toast[class*="bp3-intent-"] .bp3-button::after{
    background:rgba(255, 255, 255, 0.3) !important; }
  .bp3-toast.bp3-intent-primary{
    background-color:#137cbd;
    color:#ffffff; }
  .bp3-toast.bp3-intent-success{
    background-color:#0f9960;
    color:#ffffff; }
  .bp3-toast.bp3-intent-warning{
    background-color:#d9822b;
    color:#ffffff; }
  .bp3-toast.bp3-intent-danger{
    background-color:#db3737;
    color:#ffffff; }

.bp3-toast-message{
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  padding:11px;
  word-break:break-word; }

.bp3-toast-container{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box !important;
  display:-ms-flexbox !important;
  display:flex !important;
  -webkit-box-orient:vertical;
  -webkit-box-direction:normal;
      -ms-flex-direction:column;
          flex-direction:column;
  left:0;
  overflow:hidden;
  padding:0 20px 20px;
  pointer-events:none;
  right:0;
  z-index:40; }
  .bp3-toast-container.bp3-toast-container-in-portal{
    position:fixed; }
  .bp3-toast-container.bp3-toast-container-inline{
    position:absolute; }
  .bp3-toast-container.bp3-toast-container-top{
    top:0; }
  .bp3-toast-container.bp3-toast-container-bottom{
    bottom:0;
    -webkit-box-orient:vertical;
    -webkit-box-direction:reverse;
        -ms-flex-direction:column-reverse;
            flex-direction:column-reverse;
    top:auto; }
  .bp3-toast-container.bp3-toast-container-left{
    -webkit-box-align:start;
        -ms-flex-align:start;
            align-items:flex-start; }
  .bp3-toast-container.bp3-toast-container-right{
    -webkit-box-align:end;
        -ms-flex-align:end;
            align-items:flex-end; }

.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-enter:not(.bp3-toast-enter-active) ~ .bp3-toast, .bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active),
.bp3-toast-container-bottom .bp3-toast.bp3-toast-appear:not(.bp3-toast-appear-active) ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-exit-active ~ .bp3-toast,
.bp3-toast-container-bottom .bp3-toast.bp3-toast-leave-active ~ .bp3-toast{
  -webkit-transform:translateY(60px);
          transform:translateY(60px); }
.bp3-tooltip{
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 2px 4px rgba(16, 22, 26, 0.2), 0 8px 24px rgba(16, 22, 26, 0.2);
  -webkit-transform:scale(1);
          transform:scale(1); }
  .bp3-tooltip .bp3-popover-arrow{
    height:22px;
    position:absolute;
    width:22px; }
    .bp3-tooltip .bp3-popover-arrow::before{
      height:14px;
      margin:4px;
      width:14px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip{
    margin-bottom:11px;
    margin-top:-11px; }
    .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
      bottom:-8px; }
      .bp3-tether-element-attached-bottom.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(-90deg);
                transform:rotate(-90deg); }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip{
    margin-left:11px; }
    .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
      left:-8px; }
      .bp3-tether-element-attached-left.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(0);
                transform:rotate(0); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip{
    margin-top:11px; }
    .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
      top:-8px; }
      .bp3-tether-element-attached-top.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(90deg);
                transform:rotate(90deg); }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip{
    margin-left:-11px;
    margin-right:11px; }
    .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
      right:-8px; }
      .bp3-tether-element-attached-right.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow svg{
        -webkit-transform:rotate(180deg);
                transform:rotate(180deg); }
  .bp3-tether-element-attached-middle > .bp3-tooltip > .bp3-popover-arrow{
    top:50%;
    -webkit-transform:translateY(-50%);
            transform:translateY(-50%); }
  .bp3-tether-element-attached-center > .bp3-tooltip > .bp3-popover-arrow{
    right:50%;
    -webkit-transform:translateX(50%);
            transform:translateX(50%); }
  .bp3-tether-element-attached-top.bp3-tether-target-attached-top > .bp3-tooltip > .bp3-popover-arrow{
    top:-0.22183px; }
  .bp3-tether-element-attached-right.bp3-tether-target-attached-right > .bp3-tooltip > .bp3-popover-arrow{
    right:-0.22183px; }
  .bp3-tether-element-attached-left.bp3-tether-target-attached-left > .bp3-tooltip > .bp3-popover-arrow{
    left:-0.22183px; }
  .bp3-tether-element-attached-bottom.bp3-tether-target-attached-bottom > .bp3-tooltip > .bp3-popover-arrow{
    bottom:-0.22183px; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:top left;
            transform-origin:top left; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:top center;
            transform-origin:top center; }
  .bp3-tether-element-attached-top.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:top right;
            transform-origin:top right; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:center left;
            transform-origin:center left; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:center center;
            transform-origin:center center; }
  .bp3-tether-element-attached-middle.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:center right;
            transform-origin:center right; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-left > .bp3-tooltip{
    -webkit-transform-origin:bottom left;
            transform-origin:bottom left; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-center > .bp3-tooltip{
    -webkit-transform-origin:bottom center;
            transform-origin:bottom center; }
  .bp3-tether-element-attached-bottom.bp3-tether-element-attached-right > .bp3-tooltip{
    -webkit-transform-origin:bottom right;
            transform-origin:bottom right; }
  .bp3-tooltip .bp3-popover-content{
    background:#394b59;
    color:#f5f8fa; }
  .bp3-tooltip .bp3-popover-arrow::before{
    -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2);
            box-shadow:1px 1px 6px rgba(16, 22, 26, 0.2); }
  .bp3-tooltip .bp3-popover-arrow-border{
    fill:#10161a;
    fill-opacity:0.1; }
  .bp3-tooltip .bp3-popover-arrow-fill{
    fill:#394b59; }
  .bp3-popover-enter > .bp3-tooltip, .bp3-popover-appear > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8); }
  .bp3-popover-enter-active > .bp3-tooltip, .bp3-popover-appear-active > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-popover-exit > .bp3-tooltip{
    -webkit-transform:scale(1);
            transform:scale(1); }
  .bp3-popover-exit-active > .bp3-tooltip{
    -webkit-transform:scale(0.8);
            transform:scale(0.8);
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:100ms;
            transition-duration:100ms;
    -webkit-transition-property:-webkit-transform;
    transition-property:-webkit-transform;
    transition-property:transform;
    transition-property:transform, -webkit-transform;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tooltip .bp3-popover-content{
    padding:10px 12px; }
  .bp3-tooltip.bp3-dark,
  .bp3-dark .bp3-tooltip{
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 2px 4px rgba(16, 22, 26, 0.4), 0 8px 24px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-content,
    .bp3-dark .bp3-tooltip .bp3-popover-content{
      background:#e1e8ed;
      color:#394b59; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow::before,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow::before{
      -webkit-box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4);
              box-shadow:1px 1px 6px rgba(16, 22, 26, 0.4); }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-border,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-border{
      fill:#10161a;
      fill-opacity:0.2; }
    .bp3-tooltip.bp3-dark .bp3-popover-arrow-fill,
    .bp3-dark .bp3-tooltip .bp3-popover-arrow-fill{
      fill:#e1e8ed; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-content{
    background:#137cbd;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-primary .bp3-popover-arrow-fill{
    fill:#137cbd; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-content{
    background:#0f9960;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-success .bp3-popover-arrow-fill{
    fill:#0f9960; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-content{
    background:#d9822b;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-warning .bp3-popover-arrow-fill{
    fill:#d9822b; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-content{
    background:#db3737;
    color:#ffffff; }
  .bp3-tooltip.bp3-intent-danger .bp3-popover-arrow-fill{
    fill:#db3737; }

.bp3-tooltip-indicator{
  border-bottom:dotted 1px;
  cursor:help; }
.bp3-tree .bp3-icon, .bp3-tree .bp3-icon-standard, .bp3-tree .bp3-icon-large{
  color:#5c7080; }
  .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-tree .bp3-icon.bp3-intent-success, .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-tree-node-list{
  list-style:none;
  margin:0;
  padding-left:0; }

.bp3-tree-root{
  background-color:transparent;
  cursor:default;
  padding-left:0;
  position:relative; }

.bp3-tree-node-content-0{
  padding-left:0px; }

.bp3-tree-node-content-1{
  padding-left:23px; }

.bp3-tree-node-content-2{
  padding-left:46px; }

.bp3-tree-node-content-3{
  padding-left:69px; }

.bp3-tree-node-content-4{
  padding-left:92px; }

.bp3-tree-node-content-5{
  padding-left:115px; }

.bp3-tree-node-content-6{
  padding-left:138px; }

.bp3-tree-node-content-7{
  padding-left:161px; }

.bp3-tree-node-content-8{
  padding-left:184px; }

.bp3-tree-node-content-9{
  padding-left:207px; }

.bp3-tree-node-content-10{
  padding-left:230px; }

.bp3-tree-node-content-11{
  padding-left:253px; }

.bp3-tree-node-content-12{
  padding-left:276px; }

.bp3-tree-node-content-13{
  padding-left:299px; }

.bp3-tree-node-content-14{
  padding-left:322px; }

.bp3-tree-node-content-15{
  padding-left:345px; }

.bp3-tree-node-content-16{
  padding-left:368px; }

.bp3-tree-node-content-17{
  padding-left:391px; }

.bp3-tree-node-content-18{
  padding-left:414px; }

.bp3-tree-node-content-19{
  padding-left:437px; }

.bp3-tree-node-content-20{
  padding-left:460px; }

.bp3-tree-node-content{
  -webkit-box-align:center;
      -ms-flex-align:center;
          align-items:center;
  display:-webkit-box;
  display:-ms-flexbox;
  display:flex;
  height:30px;
  padding-right:5px;
  width:100%; }
  .bp3-tree-node-content:hover{
    background-color:rgba(191, 204, 214, 0.4); }

.bp3-tree-node-caret,
.bp3-tree-node-caret-none{
  min-width:30px; }

.bp3-tree-node-caret{
  color:#5c7080;
  cursor:pointer;
  padding:7px;
  -webkit-transform:rotate(0deg);
          transform:rotate(0deg);
  -webkit-transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:-webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9);
  transition:transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9), -webkit-transform 200ms cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-tree-node-caret:hover{
    color:#182026; }
  .bp3-dark .bp3-tree-node-caret{
    color:#a7b6c2; }
    .bp3-dark .bp3-tree-node-caret:hover{
      color:#f5f8fa; }
  .bp3-tree-node-caret.bp3-tree-node-caret-open{
    -webkit-transform:rotate(90deg);
            transform:rotate(90deg); }
  .bp3-tree-node-caret.bp3-icon-standard::before{
    content:""; }

.bp3-tree-node-icon{
  margin-right:7px;
  position:relative; }

.bp3-tree-node-label{
  overflow:hidden;
  text-overflow:ellipsis;
  white-space:nowrap;
  word-wrap:normal;
  -webkit-box-flex:1;
      -ms-flex:1 1 auto;
          flex:1 1 auto;
  position:relative;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-label span{
    display:inline; }

.bp3-tree-node-secondary-label{
  padding:0 5px;
  -webkit-user-select:none;
     -moz-user-select:none;
      -ms-user-select:none;
          user-select:none; }
  .bp3-tree-node-secondary-label .bp3-popover-wrapper,
  .bp3-tree-node-secondary-label .bp3-popover-target{
    -webkit-box-align:center;
        -ms-flex-align:center;
            align-items:center;
    display:-webkit-box;
    display:-ms-flexbox;
    display:flex; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-content{
  background-color:inherit;
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-disabled .bp3-tree-node-caret,
.bp3-tree-node.bp3-disabled .bp3-tree-node-icon{
  color:rgba(92, 112, 128, 0.6);
  cursor:not-allowed; }

.bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content,
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-standard, .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-icon-large{
    color:#ffffff; }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret::before{
    color:rgba(255, 255, 255, 0.7); }
  .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content .bp3-tree-node-caret:hover::before{
    color:#ffffff; }

.bp3-dark .bp3-tree-node-content:hover{
  background-color:rgba(92, 112, 128, 0.3); }

.bp3-dark .bp3-tree .bp3-icon, .bp3-dark .bp3-tree .bp3-icon-standard, .bp3-dark .bp3-tree .bp3-icon-large{
  color:#a7b6c2; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-primary, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-primary{
    color:#137cbd; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-success, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-success{
    color:#0f9960; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-warning, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-warning{
    color:#d9822b; }
  .bp3-dark .bp3-tree .bp3-icon.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-standard.bp3-intent-danger, .bp3-dark .bp3-tree .bp3-icon-large.bp3-intent-danger{
    color:#db3737; }

.bp3-dark .bp3-tree-node.bp3-tree-node-selected > .bp3-tree-node-content{
  background-color:#137cbd; }
.bp3-omnibar{
  -webkit-filter:blur(0);
          filter:blur(0);
  opacity:1;
  background-color:#ffffff;
  border-radius:3px;
  -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
          box-shadow:0 0 0 1px rgba(16, 22, 26, 0.1), 0 4px 8px rgba(16, 22, 26, 0.2), 0 18px 46px 6px rgba(16, 22, 26, 0.2);
  left:calc(50% - 250px);
  top:20vh;
  width:500px;
  z-index:21; }
  .bp3-omnibar.bp3-overlay-enter, .bp3-omnibar.bp3-overlay-appear{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2; }
  .bp3-omnibar.bp3-overlay-enter-active, .bp3-omnibar.bp3-overlay-appear-active{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar.bp3-overlay-exit{
    -webkit-filter:blur(0);
            filter:blur(0);
    opacity:1; }
  .bp3-omnibar.bp3-overlay-exit-active{
    -webkit-filter:blur(20px);
            filter:blur(20px);
    opacity:0.2;
    -webkit-transition-delay:0;
            transition-delay:0;
    -webkit-transition-duration:200ms;
            transition-duration:200ms;
    -webkit-transition-property:opacity, -webkit-filter;
    transition-property:opacity, -webkit-filter;
    transition-property:filter, opacity;
    transition-property:filter, opacity, -webkit-filter;
    -webkit-transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9);
            transition-timing-function:cubic-bezier(0.4, 1, 0.75, 0.9); }
  .bp3-omnibar .bp3-input{
    background-color:transparent;
    border-radius:0; }
    .bp3-omnibar .bp3-input, .bp3-omnibar .bp3-input:focus{
      -webkit-box-shadow:none;
              box-shadow:none; }
  .bp3-omnibar .bp3-menu{
    background-color:transparent;
    border-radius:0;
    -webkit-box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
            box-shadow:inset 0 1px 0 rgba(16, 22, 26, 0.15);
    max-height:calc(60vh - 40px);
    overflow:auto; }
    .bp3-omnibar .bp3-menu:empty{
      display:none; }
  .bp3-dark .bp3-omnibar, .bp3-omnibar.bp3-dark{
    background-color:#30404d;
    -webkit-box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4);
            box-shadow:0 0 0 1px rgba(16, 22, 26, 0.2), 0 4px 8px rgba(16, 22, 26, 0.4), 0 18px 46px 6px rgba(16, 22, 26, 0.4); }

.bp3-omnibar-overlay .bp3-overlay-backdrop{
  background-color:rgba(16, 22, 26, 0.2); }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }

.bp3-multi-select{
  min-width:150px; }

.bp3-multi-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto; }

.bp3-select-popover .bp3-popover-content{
  padding:5px; }

.bp3-select-popover .bp3-input-group{
  margin-bottom:0; }

.bp3-select-popover .bp3-menu{
  max-height:300px;
  max-width:400px;
  overflow:auto;
  padding:0; }
  .bp3-select-popover .bp3-menu:not(:first-child){
    padding-top:5px; }
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1pY29uLWJyYW5kMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNmZmYiPgogICAgPHBhdGggZD0iTTEwNSAxMjcuM2g0MHYxMi44aC00MHpNNTEuMSA3N0w3NCA5OS45bC0yMy4zIDIzLjMgMTAuNSAxMC41IDIzLjMtMjMuM0w5NSA5OS45IDg0LjUgODkuNCA2MS42IDY2LjV6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMSBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNGOUE4MjUiPgogICAgPHBhdGggZD0iTTIwLjIgMTEuOGMtMS42IDAtMS43LjUtMS43IDEgMCAuNC4xLjkuMSAxLjMuMS41LjEuOS4xIDEuMyAwIDEuNy0xLjQgMi4zLTMuNSAyLjNoLS45di0xLjloLjVjMS4xIDAgMS40IDAgMS40LS44IDAtLjMgMC0uNi0uMS0xIDAtLjQtLjEtLjgtLjEtMS4yIDAtMS4zIDAtMS44IDEuMy0yLTEuMy0uMi0xLjMtLjctMS4zLTIgMC0uNC4xLS44LjEtMS4yLjEtLjQuMS0uNy4xLTEgMC0uOC0uNC0uNy0xLjQtLjhoLS41VjQuMWguOWMyLjIgMCAzLjUuNyAzLjUgMi4zIDAgLjQtLjEuOS0uMSAxLjMtLjEuNS0uMS45LS4xIDEuMyAwIC41LjIgMSAxLjcgMXYxLjh6TTEuOCAxMC4xYzEuNiAwIDEuNy0uNSAxLjctMSAwLS40LS4xLS45LS4xLTEuMy0uMS0uNS0uMS0uOS0uMS0xLjMgMC0xLjYgMS40LTIuMyAzLjUtMi4zaC45djEuOWgtLjVjLTEgMC0xLjQgMC0xLjQuOCAwIC4zIDAgLjYuMSAxIDAgLjIuMS42LjEgMSAwIDEuMyAwIDEuOC0xLjMgMkM2IDExLjIgNiAxMS43IDYgMTNjMCAuNC0uMS44LS4xIDEuMi0uMS4zLS4xLjctLjEgMSAwIC44LjMuOCAxLjQuOGguNXYxLjloLS45Yy0yLjEgMC0zLjUtLjYtMy41LTIuMyAwLS40LjEtLjkuMS0xLjMuMS0uNS4xLS45LjEtMS4zIDAtLjUtLjItMS0xLjctMXYtMS45eiIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSIxMy44IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY3g9IjExIiBjeT0iOC4yIiByPSIyLjEiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgPGcgY2xhc3M9ImpwLWljb24td2FybjAiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4=);
  --jp-icon-listings-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1MC45NzggNTAuOTc4IiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCA1MC45NzggNTAuOTc4OyIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSI+Cgk8Zz4KCQk8cGF0aCBzdHlsZT0iZmlsbDojMDEwMDAyOyIgZD0iTTQzLjUyLDcuNDU4QzM4LjcxMSwyLjY0OCwzMi4zMDcsMCwyNS40ODksMEMxOC42NywwLDEyLjI2NiwyLjY0OCw3LjQ1OCw3LjQ1OAoJCQljLTkuOTQzLDkuOTQxLTkuOTQzLDI2LjExOSwwLDM2LjA2MmM0LjgwOSw0LjgwOSwxMS4yMTIsNy40NTYsMTguMDMxLDcuNDU4YzAsMCwwLjAwMSwwLDAuMDAyLDAKCQkJYzYuODE2LDAsMTMuMjIxLTIuNjQ4LDE4LjAyOS03LjQ1OGM0LjgwOS00LjgwOSw3LjQ1Ny0xMS4yMTIsNy40NTctMTguMDNDNTAuOTc3LDE4LjY3LDQ4LjMyOCwxMi4yNjYsNDMuNTIsNy40NTh6CgkJCSBNNDIuMTA2LDQyLjEwNWMtNC40MzIsNC40MzEtMTAuMzMyLDYuODcyLTE2LjYxNSw2Ljg3MmgtMC4wMDJjLTYuMjg1LTAuMDAxLTEyLjE4Ny0yLjQ0MS0xNi42MTctNi44NzIKCQkJYy05LjE2Mi05LjE2My05LjE2Mi0yNC4wNzEsMC0zMy4yMzNDMTMuMzAzLDQuNDQsMTkuMjA0LDIsMjUuNDg5LDJjNi4yODQsMCwxMi4xODYsMi40NCwxNi42MTcsNi44NzIKCQkJYzQuNDMxLDQuNDMxLDYuODcxLDEwLjMzMiw2Ljg3MSwxNi42MTdDNDguOTc3LDMxLjc3Miw0Ni41MzYsMzcuNjc1LDQyLjEwNiw0Mi4xMDV6Ii8+CgkJPHBhdGggc3R5bGU9ImZpbGw6IzAxMDAwMjsiIGQ9Ik0yMy41NzgsMzIuMjE4Yy0wLjAyMy0xLjczNCwwLjE0My0zLjA1OSwwLjQ5Ni0zLjk3MmMwLjM1My0wLjkxMywxLjExLTEuOTk3LDIuMjcyLTMuMjUzCgkJCWMwLjQ2OC0wLjUzNiwwLjkyMy0xLjA2MiwxLjM2Ny0xLjU3NWMwLjYyNi0wLjc1MywxLjEwNC0xLjQ3OCwxLjQzNi0yLjE3NWMwLjMzMS0wLjcwNywwLjQ5NS0xLjU0MSwwLjQ5NS0yLjUKCQkJYzAtMS4wOTYtMC4yNi0yLjA4OC0wLjc3OS0yLjk3OWMtMC41NjUtMC44NzktMS41MDEtMS4zMzYtMi44MDYtMS4zNjljLTEuODAyLDAuMDU3LTIuOTg1LDAuNjY3LTMuNTUsMS44MzIKCQkJYy0wLjMwMSwwLjUzNS0wLjUwMywxLjE0MS0wLjYwNywxLjgxNGMtMC4xMzksMC43MDctMC4yMDcsMS40MzItMC4yMDcsMi4xNzRoLTIuOTM3Yy0wLjA5MS0yLjIwOCwwLjQwNy00LjExNCwxLjQ5My01LjcxOQoJCQljMS4wNjItMS42NCwyLjg1NS0yLjQ4MSw1LjM3OC0yLjUyN2MyLjE2LDAuMDIzLDMuODc0LDAuNjA4LDUuMTQxLDEuNzU4YzEuMjc4LDEuMTYsMS45MjksMi43NjQsMS45NSw0LjgxMQoJCQljMCwxLjE0Mi0wLjEzNywyLjExMS0wLjQxLDIuOTExYy0wLjMwOSwwLjg0NS0wLjczMSwxLjU5My0xLjI2OCwyLjI0M2MtMC40OTIsMC42NS0xLjA2OCwxLjMxOC0xLjczLDIuMDAyCgkJCWMtMC42NSwwLjY5Ny0xLjMxMywxLjQ3OS0xLjk4NywyLjM0NmMtMC4yMzksMC4zNzctMC40MjksMC43NzctMC41NjUsMS4xOTljLTAuMTYsMC45NTktMC4yMTcsMS45NTEtMC4xNzEsMi45NzkKCQkJQzI2LjU4OSwzMi4yMTgsMjMuNTc4LDMyLjIxOCwyMy41NzgsMzIuMjE4eiBNMjMuNTc4LDM4LjIydi0zLjQ4NGgzLjA3NnYzLjQ4NEgyMy41Nzh6Ii8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMEQ0N0ExIj4KICAgIDxwYXRoIGQ9Ik0xMS4xIDYuOVY1LjhINi45YzAtLjUgMC0xLjMuMi0xLjYuNC0uNy44LTEuMSAxLjctMS40IDEuNy0uMyAyLjUtLjMgMy45LS4xIDEgLjEgMS45LjkgMS45IDEuOXY0LjJjMCAuNS0uOSAxLjYtMiAxLjZIOC44Yy0xLjUgMC0yLjQgMS40LTIuNCAyLjh2Mi4ySDQuN0MzLjUgMTUuMSAzIDE0IDMgMTMuMVY5Yy0uMS0xIC42LTIgMS44LTIgMS41LS4xIDYuMy0uMSA2LjMtLjF6Ii8+CiAgICA8cGF0aCBkPSJNMTAuOSAxNS4xdjEuMWg0LjJjMCAuNSAwIDEuMy0uMiAxLjYtLjQuNy0uOCAxLjEtMS43IDEuNC0xLjcuMy0yLjUuMy0zLjkuMS0xLS4xLTEuOS0uOS0xLjktMS45di00LjJjMC0uNS45LTEuNiAyLTEuNmgzLjhjMS41IDAgMi40LTEuNCAyLjQtMi44VjYuNmgxLjdDMTguNSA2LjkgMTkgOCAxOSA4LjlWMTNjMCAxLS43IDIuMS0xLjkgMi4xaC02LjJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiB3aWR0aD0iMjAiIGhlaWdodD0iMjAiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMikiIGZpbGw9IiMzMzMzMzMiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uLWFjY2VudDIganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGQ9Ik01LjA1NjY0IDguNzYxNzJDNS4wNTY2NCA4LjU5NzY2IDUuMDMxMjUgOC40NTMxMiA0Ljk4MDQ3IDguMzI4MTJDNC45MzM1OSA4LjE5OTIyIDQuODU1NDcgOC4wODIwMyA0Ljc0NjA5IDcuOTc2NTZDNC42NDA2MiA3Ljg3MTA5IDQuNSA3Ljc3NTM5IDQuMzI0MjIgNy42ODk0NUM0LjE1MjM0IDcuNTk5NjEgMy45NDMzNiA3LjUxMTcyIDMuNjk3MjcgNy40MjU3OEMzLjMwMjczIDcuMjg1MTYgMi45NDMzNiA3LjEzNjcyIDIuNjE5MTQgNi45ODA0N0MyLjI5NDkyIDYuODI0MjIgMi4wMTc1OCA2LjY0MjU4IDEuNzg3MTEgNi40MzU1NUMxLjU2MDU1IDYuMjI4NTIgMS4zODQ3NyA1Ljk4ODI4IDEuMjU5NzcgNS43MTQ4NEMxLjEzNDc3IDUuNDM3NSAxLjA3MjI3IDUuMTA5MzggMS4wNzIyNyA0LjczMDQ3QzEuMDcyMjcgNC4zOTg0NCAxLjEyODkxIDQuMDk1NyAxLjI0MjE5IDMuODIyMjdDMS4zNTU0NyAzLjU0NDkyIDEuNTE1NjIgMy4zMDQ2OSAxLjcyMjY2IDMuMTAxNTZDMS45Mjk2OSAyLjg5ODQ0IDIuMTc5NjkgMi43MzQzNyAyLjQ3MjY2IDIuNjA5MzhDMi43NjU2MiAyLjQ4NDM4IDMuMDkxOCAyLjQwNDMgMy40NTExNyAyLjM2OTE0VjEuMTA5MzhINC4zODg2N1YyLjM4MDg2QzQuNzQwMjMgMi40Mjc3MyA1LjA1NjY0IDIuNTIzNDQgNS4zMzc4OSAyLjY2Nzk3QzUuNjE5MTQgMi44MTI1IDUuODU3NDIgMy4wMDE5NSA2LjA1MjczIDMuMjM2MzNDNi4yNTE5NSAzLjQ2NjggNi40MDQzIDMuNzQwMjMgNi41MDk3NyA0LjA1NjY0QzYuNjE5MTQgNC4zNjkxNCA2LjY3MzgzIDQuNzIwNyA2LjY3MzgzIDUuMTExMzNINS4wNDQ5MkM1LjA0NDkyIDQuNjM4NjcgNC45Mzc1IDQuMjgxMjUgNC43MjI2NiA0LjAzOTA2QzQuNTA3ODEgMy43OTI5NyA0LjIxNjggMy42Njk5MiAzLjg0OTYxIDMuNjY5OTJDMy42NTAzOSAzLjY2OTkyIDMuNDc2NTYgMy42OTcyNyAzLjMyODEyIDMuNzUxOTVDMy4xODM1OSAzLjgwMjczIDMuMDY0NDUgMy44NzY5NSAyLjk3MDcgMy45NzQ2MUMyLjg3Njk1IDQuMDY4MzYgMi44MDY2NCA0LjE3OTY5IDIuNzU5NzcgNC4zMDg1OUMyLjcxNjggNC40Mzc1IDIuNjk1MzEgNC41NzgxMiAyLjY5NTMxIDQuNzMwNDdDMi42OTUzMSA0Ljg4MjgxIDIuNzE2OCA1LjAxOTUzIDIuNzU5NzcgNS4xNDA2MkMyLjgwNjY0IDUuMjU3ODEgMi44ODI4MSA1LjM2NzE5IDIuOTg4MjggNS40Njg3NUMzLjA5NzY2IDUuNTcwMzEgMy4yNDAyMyA1LjY2Nzk3IDMuNDE2MDIgNS43NjE3MkMzLjU5MTggNS44NTE1NiAzLjgxMDU1IDUuOTQzMzYgNC4wNzIyNyA2LjAzNzExQzQuNDY2OCA2LjE4NTU1IDQuODI0MjIgNi4zMzk4NCA1LjE0NDUzIDYuNUM1LjQ2NDg0IDYuNjU2MjUgNS43MzgyOCA2LjgzOTg0IDUuOTY0ODQgNy4wNTA3OEM2LjE5NTMxIDcuMjU3ODEgNi4zNzEwOSA3LjUgNi40OTIxOSA3Ljc3NzM0QzYuNjE3MTkgOC4wNTA3OCA2LjY3OTY5IDguMzc1IDYuNjc5NjkgOC43NUM2LjY3OTY5IDkuMDkzNzUgNi42MjMwNSA5LjQwNDMgNi41MDk3NyA5LjY4MTY0QzYuMzk2NDggOS45NTUwOCA2LjIzNDM4IDEwLjE5MTQgNi4wMjM0NCAxMC4zOTA2QzUuODEyNSAxMC41ODk4IDUuNTU4NTkgMTAuNzUgNS4yNjE3MiAxMC44NzExQzQuOTY0ODQgMTAuOTg4MyA0LjYzMjgxIDExLjA2NDUgNC4yNjU2MiAxMS4wOTk2VjEyLjI0OEgzLjMzMzk4VjExLjA5OTZDMy4wMDE5NSAxMS4wNjg0IDIuNjc5NjkgMTAuOTk2MSAyLjM2NzE5IDEwLjg4MjhDMi4wNTQ2OSAxMC43NjU2IDEuNzc3MzQgMTAuNTk3NyAxLjUzNTE2IDEwLjM3ODlDMS4yOTY4OCAxMC4xNjAyIDEuMTA1NDcgOS44ODQ3NyAwLjk2MDkzOCA5LjU1MjczQzAuODE2NDA2IDkuMjE2OCAwLjc0NDE0MSA4LjgxNDQ1IDAuNzQ0MTQxIDguMzQ1N0gyLjM3ODkxQzIuMzc4OTEgOC42MjY5NSAyLjQxOTkyIDguODYzMjggMi41MDE5NSA5LjA1NDY5QzIuNTgzOTggOS4yNDIxOSAyLjY4OTQ1IDkuMzkyNTggMi44MTgzNiA5LjUwNTg2QzIuOTUxMTcgOS42MTUyMyAzLjEwMTU2IDkuNjkzMzYgMy4yNjk1MyA5Ljc0MDIzQzMuNDM3NSA5Ljc4NzExIDMuNjA5MzggOS44MTA1NSAzLjc4NTE2IDkuODEwNTVDNC4yMDMxMiA5LjgxMDU1IDQuNTE5NTMgOS43MTI4OSA0LjczNDM4IDkuNTE3NThDNC45NDkyMiA5LjMyMjI3IDUuMDU2NjQgOS4wNzAzMSA1LjA1NjY0IDguNzYxNzJaTTEzLjQxOCAxMi4yNzE1SDguMDc0MjJWMTFIMTMuNDE4VjEyLjI3MTVaIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzLjk1MjY0IDYpIiBmaWxsPSJ3aGl0ZSIvPgo8L3N2Zz4K);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTUgMTVIM3YyaDEydi0yem0wLThIM3YyaDEyVjd6TTMgMTNoMTh2LTJIM3Yyem0wIDhoMTh2LTJIM3Yyek0zIDN2MmgxOFYzSDN6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4=);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}
.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}
.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}
.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}
.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}
.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}
.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}
.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}
.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}
.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}
.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}
.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}
.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}
.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}
.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}
.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}
.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}
.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}
.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}
.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}
.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}
.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}
.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}
.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}
.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}
.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}
.jp-FileIcon {
  background-image: var(--jp-icon-file);
}
.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}
.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}
.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}
.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}
.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}
.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}
.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}
.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}
.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}
.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}
.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}
.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}
.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}
.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}
.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}
.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}
.jp-ListIcon {
  background-image: var(--jp-icon-list);
}
.jp-ListingsInfoIcon {
  background-image: var(--jp-icon-listings-info);
}
.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}
.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}
.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}
.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}
.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}
.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}
.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}
.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}
.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}
.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}
.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}
.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}
.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}
.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}
.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}
.jp-RunIcon {
  background-image: var(--jp-icon-run);
}
.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}
.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}
.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}
.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}
.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}
.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}
.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}
.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}
.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}
.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}
.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}
.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}
.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}
.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}
.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}
.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}
.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}
/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}
/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}
/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}
.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}
.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}
.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}
.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}
.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}
.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}
.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}
.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}
/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}
.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}
.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}
.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}
.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}
.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}
.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}
/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}
.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}
.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}
.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

/* CSS for icons in selected items in the settings editor */
#setting-editor .jp-PluginList .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
#setting-editor
  .jp-PluginList
  .jp-mod-selected
  .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* CSS for icons in selected tabs in the sidebar tab manager */
#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable[fill] {
  fill: #fff;
}

#tab-manager .lm-TabBar-tab.jp-mod-active .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable[fill] {
  fill: var(--jp-brand-color1);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-active
  .jp-icon-hover
  :hover
  .jp-icon-selectable-inverse[fill] {
  fill: #fff;
}

/**
 * TODO: come up with non css-hack solution for showing the busy icon on top
 *  of the close icon
 * CSS for complex behavior of close icon of tabs in the sidebar tab manager
 */
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
#tab-manager
  .lm-TabBar-tab.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

#tab-manager
  .lm-TabBar-tab.jp-mod-dirty.jp-mod-active
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: #fff;
}

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}
/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) svg {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-border-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0px;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-warn-color0);
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

/* Override Blueprint's _reset.scss styles */
html {
  box-sizing: unset;
}

*,
*::before,
*::after {
  box-sizing: unset;
}

body {
  color: unset;
  font-family: var(--jp-ui-font-family);
}

p {
  margin-top: unset;
  margin-bottom: unset;
}

small {
  font-size: unset;
}

strong {
  font-weight: unset;
}

/* Override Blueprint's _typography.scss styles */
a {
  text-decoration: unset;
  color: unset;
}
a:hover {
  text-decoration: unset;
  color: unset;
}

/* Override Blueprint's _accessibility.scss styles */
:focus {
  outline: unset;
  outline-offset: unset;
  -moz-outline-radius: unset;
}

/* Styles for ui-components */
.jp-Button {
  border-radius: var(--jp-border-radius);
  padding: 0px 12px;
  font-size: var(--jp-ui-font-size1);
}

/* Use our own theme for hover styles */
button.jp-Button.bp3-button.bp3-minimal:hover {
  background-color: var(--jp-layout-color2);
}
.jp-Button.minimal {
  color: unset !important;
}

.jp-Button.jp-ToolbarButtonComponent {
  text-transform: none;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color3);
}

.jp-BPIcon {
  display: inline-block;
  vertical-align: middle;
  margin: auto;
}

/* Stop blueprint futzing with our icon fills */
.bp3-icon.jp-BPIcon > svg:not([fill]) {
  fill: var(--jp-inverse-layout-color3);
}

.jp-InputGroupAction {
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

/* Use our own theme for hover and option styles */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}
select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-top: 1px solid var(--jp-border-color2);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-Collapse-header {
  padding: 1px 12px;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size2);
}

.jp-Collapse-header:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Collapse-contents {
  padding: 0px 12px 0px 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0px;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0px 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px 5px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0px;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty:after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0px 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0px;
  left: 0px;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px;
  padding-bottom: 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0px;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0px 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

.jp-HoverBox.jp-mod-outofview {
  display: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;

  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;

  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #aa00ff;

  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;

  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;

  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;

  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;

  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;

  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;

  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;

  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;

  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;

  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ffff00;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;

  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;

  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;

  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;

  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;

  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eeeeee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;

  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent:before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent:after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0px 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FileDialog-Checkbox {
  margin-top: 35px;
  display: flex;
  flex-direction: row;
  align-items: end;
  width: 100%;
}

.jp-FileDialog-Checkbox > label {
  flex: 1 1 auto;
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  height: 28px;
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  background-color: var(--jp-layout-color1);
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0px 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  height: 32px;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 1;
  overflow-x: auto;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px;
  margin: 0px;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0px 6px;
  margin: 0px;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent span {
  padding: 0px;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/


/* <DEPRECATED> */ body.p-mod-override-cursor *, /* </DEPRECATED> */
body.lm-mod-override-cursor * {
  cursor: inherit !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0px;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/* BASICS */

.CodeMirror {
  /* Set height, width, borders, and global font properties here */
  font-family: monospace;
  height: 300px;
  color: black;
  direction: ltr;
}

/* PADDING */

.CodeMirror-lines {
  padding: 4px 0; /* Vertical padding around content */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  padding: 0 4px; /* Horizontal padding of content */
}

.CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  background-color: white; /* The little square between H and V scrollbars */
}

/* GUTTER */

.CodeMirror-gutters {
  border-right: 1px solid #ddd;
  background-color: #f7f7f7;
  white-space: nowrap;
}
.CodeMirror-linenumbers {}
.CodeMirror-linenumber {
  padding: 0 3px 0 5px;
  min-width: 20px;
  text-align: right;
  color: #999;
  white-space: nowrap;
}

.CodeMirror-guttermarker { color: black; }
.CodeMirror-guttermarker-subtle { color: #999; }

/* CURSOR */

.CodeMirror-cursor {
  border-left: 1px solid black;
  border-right: none;
  width: 0;
}
/* Shown when moving in bi-directional text */
.CodeMirror div.CodeMirror-secondarycursor {
  border-left: 1px solid silver;
}
.cm-fat-cursor .CodeMirror-cursor {
  width: auto;
  border: 0 !important;
  background: #7e7;
}
.cm-fat-cursor div.CodeMirror-cursors {
  z-index: 1;
}
.cm-fat-cursor-mark {
  background-color: rgba(20, 255, 20, 0.5);
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
}
.cm-animate-fat-cursor {
  width: auto;
  border: 0;
  -webkit-animation: blink 1.06s steps(1) infinite;
  -moz-animation: blink 1.06s steps(1) infinite;
  animation: blink 1.06s steps(1) infinite;
  background-color: #7e7;
}
@-moz-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@-webkit-keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}
@keyframes blink {
  0% {}
  50% { background-color: transparent; }
  100% {}
}

/* Can style cursor different in overwrite (non-insert) mode */
.CodeMirror-overwrite .CodeMirror-cursor {}

.cm-tab { display: inline-block; text-decoration: inherit; }

.CodeMirror-rulers {
  position: absolute;
  left: 0; right: 0; top: -50px; bottom: 0;
  overflow: hidden;
}
.CodeMirror-ruler {
  border-left: 1px solid #ccc;
  top: 0; bottom: 0;
  position: absolute;
}

/* DEFAULT THEME */

.cm-s-default .cm-header {color: blue;}
.cm-s-default .cm-quote {color: #090;}
.cm-negative {color: #d44;}
.cm-positive {color: #292;}
.cm-header, .cm-strong {font-weight: bold;}
.cm-em {font-style: italic;}
.cm-link {text-decoration: underline;}
.cm-strikethrough {text-decoration: line-through;}

.cm-s-default .cm-keyword {color: #708;}
.cm-s-default .cm-atom {color: #219;}
.cm-s-default .cm-number {color: #164;}
.cm-s-default .cm-def {color: #00f;}
.cm-s-default .cm-variable,
.cm-s-default .cm-punctuation,
.cm-s-default .cm-property,
.cm-s-default .cm-operator {}
.cm-s-default .cm-variable-2 {color: #05a;}
.cm-s-default .cm-variable-3, .cm-s-default .cm-type {color: #085;}
.cm-s-default .cm-comment {color: #a50;}
.cm-s-default .cm-string {color: #a11;}
.cm-s-default .cm-string-2 {color: #f50;}
.cm-s-default .cm-meta {color: #555;}
.cm-s-default .cm-qualifier {color: #555;}
.cm-s-default .cm-builtin {color: #30a;}
.cm-s-default .cm-bracket {color: #997;}
.cm-s-default .cm-tag {color: #170;}
.cm-s-default .cm-attribute {color: #00c;}
.cm-s-default .cm-hr {color: #999;}
.cm-s-default .cm-link {color: #00c;}

.cm-s-default .cm-error {color: #f00;}
.cm-invalidchar {color: #f00;}

.CodeMirror-composing { border-bottom: 2px solid; }

/* Default styles for common addons */

div.CodeMirror span.CodeMirror-matchingbracket {color: #0b0;}
div.CodeMirror span.CodeMirror-nonmatchingbracket {color: #a22;}
.CodeMirror-matchingtag { background: rgba(255, 150, 0, .3); }
.CodeMirror-activeline-background {background: #e8f2ff;}

/* STOP */

/* The rest of this file contains styles related to the mechanics of
   the editor. You probably shouldn't touch them. */

.CodeMirror {
  position: relative;
  overflow: hidden;
  background: white;
}

.CodeMirror-scroll {
  overflow: scroll !important; /* Things will break if this is overridden */
  /* 50px is the magic margin used to hide the element's real scrollbars */
  /* See overflow: hidden in .CodeMirror */
  margin-bottom: -50px; margin-right: -50px;
  padding-bottom: 50px;
  height: 100%;
  outline: none; /* Prevent dragging from highlighting the element */
  position: relative;
}
.CodeMirror-sizer {
  position: relative;
  border-right: 50px solid transparent;
}

/* The fake, visible scrollbars. Used to force redraw during scrolling
   before actual scrolling happens, thus preventing shaking and
   flickering artifacts. */
.CodeMirror-vscrollbar, .CodeMirror-hscrollbar, .CodeMirror-scrollbar-filler, .CodeMirror-gutter-filler {
  position: absolute;
  z-index: 6;
  display: none;
  outline: none;
}
.CodeMirror-vscrollbar {
  right: 0; top: 0;
  overflow-x: hidden;
  overflow-y: scroll;
}
.CodeMirror-hscrollbar {
  bottom: 0; left: 0;
  overflow-y: hidden;
  overflow-x: scroll;
}
.CodeMirror-scrollbar-filler {
  right: 0; bottom: 0;
}
.CodeMirror-gutter-filler {
  left: 0; bottom: 0;
}

.CodeMirror-gutters {
  position: absolute; left: 0; top: 0;
  min-height: 100%;
  z-index: 3;
}
.CodeMirror-gutter {
  white-space: normal;
  height: 100%;
  display: inline-block;
  vertical-align: top;
  margin-bottom: -50px;
}
.CodeMirror-gutter-wrapper {
  position: absolute;
  z-index: 4;
  background: none !important;
  border: none !important;
}
.CodeMirror-gutter-background {
  position: absolute;
  top: 0; bottom: 0;
  z-index: 4;
}
.CodeMirror-gutter-elt {
  position: absolute;
  cursor: default;
  z-index: 4;
}
.CodeMirror-gutter-wrapper ::selection { background-color: transparent }
.CodeMirror-gutter-wrapper ::-moz-selection { background-color: transparent }

.CodeMirror-lines {
  cursor: text;
  min-height: 1px; /* prevents collapsing before first draw */
}
.CodeMirror pre.CodeMirror-line,
.CodeMirror pre.CodeMirror-line-like {
  /* Reset some styles that the rest of the page might have set */
  -moz-border-radius: 0; -webkit-border-radius: 0; border-radius: 0;
  border-width: 0;
  background: transparent;
  font-family: inherit;
  font-size: inherit;
  margin: 0;
  white-space: pre;
  word-wrap: normal;
  line-height: inherit;
  color: inherit;
  z-index: 2;
  position: relative;
  overflow: visible;
  -webkit-tap-highlight-color: transparent;
  -webkit-font-variant-ligatures: contextual;
  font-variant-ligatures: contextual;
}
.CodeMirror-wrap pre.CodeMirror-line,
.CodeMirror-wrap pre.CodeMirror-line-like {
  word-wrap: break-word;
  white-space: pre-wrap;
  word-break: normal;
}

.CodeMirror-linebackground {
  position: absolute;
  left: 0; right: 0; top: 0; bottom: 0;
  z-index: 0;
}

.CodeMirror-linewidget {
  position: relative;
  z-index: 2;
  padding: 0.1px; /* Force widget margins to stay inside of the container */
}

.CodeMirror-widget {}

.CodeMirror-rtl pre { direction: rtl; }

.CodeMirror-code {
  outline: none;
}

/* Force content-box sizing for the elements where we expect it */
.CodeMirror-scroll,
.CodeMirror-sizer,
.CodeMirror-gutter,
.CodeMirror-gutters,
.CodeMirror-linenumber {
  -moz-box-sizing: content-box;
  box-sizing: content-box;
}

.CodeMirror-measure {
  position: absolute;
  width: 100%;
  height: 0;
  overflow: hidden;
  visibility: hidden;
}

.CodeMirror-cursor {
  position: absolute;
  pointer-events: none;
}
.CodeMirror-measure pre { position: static; }

div.CodeMirror-cursors {
  visibility: hidden;
  position: relative;
  z-index: 3;
}
div.CodeMirror-dragcursors {
  visibility: visible;
}

.CodeMirror-focused div.CodeMirror-cursors {
  visibility: visible;
}

.CodeMirror-selected { background: #d9d9d9; }
.CodeMirror-focused .CodeMirror-selected { background: #d7d4f0; }
.CodeMirror-crosshair { cursor: crosshair; }
.CodeMirror-line::selection, .CodeMirror-line > span::selection, .CodeMirror-line > span > span::selection { background: #d7d4f0; }
.CodeMirror-line::-moz-selection, .CodeMirror-line > span::-moz-selection, .CodeMirror-line > span > span::-moz-selection { background: #d7d4f0; }

.cm-searching {
  background-color: #ffa;
  background-color: rgba(255, 255, 0, .4);
}

/* Used to force a border model for a node */
.cm-force-border { padding-right: .1px; }

@media print {
  /* Hide the cursor when printing */
  .CodeMirror div.CodeMirror-cursors {
    visibility: hidden;
  }
}

/* See issue #2901 */
.cm-tab-wrap-hack:after { content: ''; }

/* Help users use markselection to safely style text background */
span.CodeMirror-selectedtext { background: none; }

.CodeMirror-dialog {
  position: absolute;
  left: 0; right: 0;
  background: inherit;
  z-index: 15;
  padding: .1em .8em;
  overflow: hidden;
  color: inherit;
}

.CodeMirror-dialog-top {
  border-bottom: 1px solid #eee;
  top: 0;
}

.CodeMirror-dialog-bottom {
  border-top: 1px solid #eee;
  bottom: 0;
}

.CodeMirror-dialog input {
  border: none;
  outline: none;
  background: transparent;
  width: 20em;
  color: inherit;
  font-family: monospace;
}

.CodeMirror-dialog button {
  font-size: 70%;
}

.CodeMirror-foldmarker {
  color: blue;
  text-shadow: #b9f 1px 1px 2px, #b9f -1px -1px 2px, #b9f 1px -1px 2px, #b9f -1px 1px 2px;
  font-family: arial;
  line-height: .3;
  cursor: pointer;
}
.CodeMirror-foldgutter {
  width: .7em;
}
.CodeMirror-foldgutter-open,
.CodeMirror-foldgutter-folded {
  cursor: pointer;
}
.CodeMirror-foldgutter-open:after {
  content: "\25BE";
}
.CodeMirror-foldgutter-folded:after {
  content: "\25B8";
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.CodeMirror {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;
  /* Changed to auto to autogrow */
}

.CodeMirror pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* This causes https://github.com/jupyter/jupyterlab/issues/522 */
/* May not cause it not because we changed it! */
.CodeMirror-lines {
  padding: var(--jp-code-padding) 0;
}

.CodeMirror-linenumber {
  padding: 0 8px;
}

.jp-CodeMirrorEditor {
  cursor: text;
}

.jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .CodeMirror-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.CodeMirror.jp-mod-readOnly .CodeMirror-cursor {
  display: none;
}

.CodeMirror-gutters {
  border-right: 1px solid var(--jp-border-color2);
  background-color: var(--jp-layout-color0);
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.CodeMirror-selectedtext.cm-searching {
  background-color: var(--jp-search-selected-match-background-color) !important;
  color: var(--jp-search-selected-match-color) !important;
}

.cm-searching {
  background-color: var(
    --jp-search-unselected-match-background-color
  ) !important;
  color: var(--jp-search-unselected-match-color) !important;
}

.CodeMirror-focused .CodeMirror-selected {
  background-color: var(--jp-editor-selected-focused-background);
}

.CodeMirror-selected {
  background-color: var(--jp-editor-selected-background);
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/**
 * Here is our jupyter theme for CodeMirror syntax highlighting
 * This is used in our marked.js syntax highlighting and CodeMirror itself
 * The string "jupyter" is set in ../codemirror/widget.DEFAULT_CODEMIRROR_THEME
 * This came from the classic notebook, which came form highlight.js/GitHub
 */

/**
 * CodeMirror themes are handling the background/color in this way. This works
 * fine for CodeMirror editors outside the notebook, but the notebook styles
 * these things differently.
 */
.CodeMirror.cm-s-jupyter {
  background: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

/* In the notebook, we want this styling to be handled by its container */
.jp-CodeConsole .CodeMirror.cm-s-jupyter,
.jp-Notebook .CodeMirror.cm-s-jupyter {
  background: transparent;
}

.cm-s-jupyter .CodeMirror-cursor {
  border-left: var(--jp-code-cursor-width0) solid var(--jp-editor-cursor-color);
}
.cm-s-jupyter span.cm-keyword {
  color: var(--jp-mirror-editor-keyword-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-atom {
  color: var(--jp-mirror-editor-atom-color);
}
.cm-s-jupyter span.cm-number {
  color: var(--jp-mirror-editor-number-color);
}
.cm-s-jupyter span.cm-def {
  color: var(--jp-mirror-editor-def-color);
}
.cm-s-jupyter span.cm-variable {
  color: var(--jp-mirror-editor-variable-color);
}
.cm-s-jupyter span.cm-variable-2 {
  color: var(--jp-mirror-editor-variable-2-color);
}
.cm-s-jupyter span.cm-variable-3 {
  color: var(--jp-mirror-editor-variable-3-color);
}
.cm-s-jupyter span.cm-punctuation {
  color: var(--jp-mirror-editor-punctuation-color);
}
.cm-s-jupyter span.cm-property {
  color: var(--jp-mirror-editor-property-color);
}
.cm-s-jupyter span.cm-operator {
  color: var(--jp-mirror-editor-operator-color);
  font-weight: bold;
}
.cm-s-jupyter span.cm-comment {
  color: var(--jp-mirror-editor-comment-color);
  font-style: italic;
}
.cm-s-jupyter span.cm-string {
  color: var(--jp-mirror-editor-string-color);
}
.cm-s-jupyter span.cm-string-2 {
  color: var(--jp-mirror-editor-string-2-color);
}
.cm-s-jupyter span.cm-meta {
  color: var(--jp-mirror-editor-meta-color);
}
.cm-s-jupyter span.cm-qualifier {
  color: var(--jp-mirror-editor-qualifier-color);
}
.cm-s-jupyter span.cm-builtin {
  color: var(--jp-mirror-editor-builtin-color);
}
.cm-s-jupyter span.cm-bracket {
  color: var(--jp-mirror-editor-bracket-color);
}
.cm-s-jupyter span.cm-tag {
  color: var(--jp-mirror-editor-tag-color);
}
.cm-s-jupyter span.cm-attribute {
  color: var(--jp-mirror-editor-attribute-color);
}
.cm-s-jupyter span.cm-header {
  color: var(--jp-mirror-editor-header-color);
}
.cm-s-jupyter span.cm-quote {
  color: var(--jp-mirror-editor-quote-color);
}
.cm-s-jupyter span.cm-link {
  color: var(--jp-mirror-editor-link-color);
}
.cm-s-jupyter span.cm-error {
  color: var(--jp-mirror-editor-error-color);
}
.cm-s-jupyter span.cm-hr {
  color: #999;
}

.cm-s-jupyter span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}

.cm-s-jupyter .CodeMirror-activeline-background,
.cm-s-jupyter .CodeMirror-gutter {
  background-color: var(--jp-layout-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .remote-caret {
  position: relative;
  border-left: 2px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .remote-caret > div {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -2px;
  font-size: 0.95em;
  background-color: rgb(250, 129, 0);
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 3;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .remote-caret.hide-name > div {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .remote-caret:hover > div {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0px;
  padding: 0px;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}
.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}
.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}
.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}
.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}
.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}
.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}
.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}
.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}
.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}
.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}
.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}
.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}
.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}
.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}
.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}
.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}
.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}
.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0em;
}

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: 12px;
  table-layout: fixed;
  margin-left: auto;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon table {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0px;
}

.jp-RenderedHTMLCommon p {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}
/* ...or leave it untouched if they don't */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-dark-background {
}
[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-light-background {
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}
.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}
.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}
.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}
.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}
.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}
.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}
.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}
.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: 0.8em;
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser {
  display: flex;
  flex-direction: column;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  border-bottom: none;
  height: auto;
  margin: var(--jp-toolbar-header-margin);
  box-shadow: none;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0px 2px;
  padding: 0px 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0px;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar.jp-Toolbar {
  padding: 0px;
  margin: 8px 12px 0px 12px;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  justify-content: flex-start;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0px;
  padding-right: 2px;
}

.jp-FileBrowser-toolbar.jp-Toolbar .jp-ToolbarButtonComponent {
  width: 40px;
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent {
  width: 72px;
  background: var(--jp-brand-color1);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent:focus-visible {
  background-color: var(--jp-brand-color0);
}

.jp-FileBrowser-toolbar.jp-Toolbar
  .jp-Toolbar-item:first-child
  .jp-ToolbarButtonComponent
  .jp-icon3 {
  fill: white;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileBrowser-filterBox {
  padding: 0px;
  flex: 0 0 auto;
  margin: 8px 12px 0px 12px;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing:focus-visible {
  border: 1px solid var(--jp-brand-color1);
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px 12px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon:before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon:before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0px;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-DirListing-deadSpace {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
}

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: flex;
  flex-direction: row;
}

body[data-format='mobile'] .jp-OutputArea-child {
  flex-direction: column;
}

.jp-OutputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-OutputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

.jp-OutputArea-output {
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea-child .jp-OutputArea-output {
  flex-grow: 1;
  flex-shrink: 1;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  margin-left: var(--jp-notebook-padding);
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `p-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated:before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0px;
  padding: 0px;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0px;
  flex: 1 1 auto;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-OutputArea-stdin {
  line-height: var(--jp-code-line-height);
  padding-top: var(--jp-code-padding);
  display: flex;
}

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;
  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0px;
  bottom: 0px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0px;
  width: 100%;
  padding: 0px;
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: flex;
  flex-direction: row;
  overflow: hidden;
}

body[data-format='mobile'] .jp-InputArea {
  flex-direction: column;
}

.jp-InputArea-editor {
  flex: 1 1 auto;
  overflow: hidden;
}

.jp-InputArea-editor {
  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0px;
  background: var(--jp-cell-editor-background);
}

body[data-format='mobile'] .jp-InputArea-editor {
  margin-left: var(--jp-notebook-padding);
}

.jp-InputPrompt {
  flex: 0 0 var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);
  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

body[data-format='mobile'] .jp-InputPrompt {
  flex: 0 0 auto;
  text-align: left;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: flex;
  flex-direction: row;
  flex: 1 1 auto;
}

.jp-Placeholder-prompt {
  box-sizing: border-box;
}

.jp-Placeholder-content {
  flex: 1 1 auto;
  border: none;
  background: transparent;
  height: 20px;
  box-sizing: border-box;
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0px;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0px;
  margin: 0px;
  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 200px;
  box-shadow: inset 0 0 6px 2px rgba(0, 0, 0, 0.3);
  margin-left: var(--jp-private-cell-scrolling-output-offset);
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  flex: 0 0
    calc(
      var(--jp-cell-prompt-width) -
        var(--jp-private-cell-scrolling-output-offset)
    );
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  flex: 1 1 auto;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

.jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
}

.jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-collapseHeadingButton {
  display: none;
}

.jp-MarkdownCell:hover .jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  position: absolute;
  right: 0;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: 2px;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook-render * {
  contain: none !important;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
  float: left;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt:before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0px;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0px rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-NotebookTools-tool {
  padding: 0px 12px 0 12px;
}

.jp-ActiveCellTool {
  padding: 12px;
  background-color: var(--jp-layout-color1);
  border-top: none !important;
}

.jp-ActiveCellTool .jp-InputArea-prompt {
  flex: 0 0 auto;
  padding-left: 0px;
}

.jp-ActiveCellTool .jp-InputArea-editor {
  flex: 1 1 auto;
  background: var(--jp-cell-editor-background);
  border-color: var(--jp-cell-editor-border-color);
}

.jp-ActiveCellTool .jp-InputArea-editor .CodeMirror {
  background: transparent;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0px 12px 0px;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body div {
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>

    <style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0px 2px 1px -1px var(--jp-shadow-umbra-color),
    0px 1px 1px 0px var(--jp-shadow-penumbra-color),
    0px 1px 3px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0px 3px 1px -2px var(--jp-shadow-umbra-color),
    0px 2px 2px 0px var(--jp-shadow-penumbra-color),
    0px 1px 5px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0px 2px 4px -1px var(--jp-shadow-umbra-color),
    0px 4px 5px 0px var(--jp-shadow-penumbra-color),
    0px 1px 10px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0px 3px 5px -1px var(--jp-shadow-umbra-color),
    0px 6px 10px 0px var(--jp-shadow-penumbra-color),
    0px 1px 18px 0px var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0px 5px 5px -3px var(--jp-shadow-umbra-color),
    0px 8px 10px 1px var(--jp-shadow-penumbra-color),
    0px 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0px 7px 8px -4px var(--jp-shadow-umbra-color),
    0px 12px 17px 2px var(--jp-shadow-penumbra-color),
    0px 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0px 8px 10px -5px var(--jp-shadow-umbra-color),
    0px 16px 24px 2px var(--jp-shadow-penumbra-color),
    0px 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0px 10px 13px -6px var(--jp-shadow-umbra-color),
    0px 20px 31px 3px var(--jp-shadow-penumbra-color),
    0px 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0px 11px 15px -7px var(--jp-shadow-umbra-color),
    0px 24px 38px 3px var(--jp-shadow-penumbra-color),
    0px 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;

  --jp-ui-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica,
    Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;

  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);

  --jp-content-link-color: var(--md-blue-700);

  --jp-content-font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Helvetica, Arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: Menlo, Consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);

  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);

  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);

  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);

  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;

  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;

  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);

  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0px;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);
  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;
  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0px 0px 2px 0px rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0px 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-border-color1);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: #05a;
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #aa22ff;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #aa22ff;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);
}
</style>

<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

.highlight  {
  margin: 0.4em;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.CodeMirror pre {
  margin: 0;
  padding: 0;
}

/* Using table instead of flexbox so that we can use break-inside property */
/* CSS rules under this comment should not be required anymore after we move to the JupyterLab 4.0 CSS */


.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  min-width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-OutputArea-child {
  display: table;
  width: 100%;
}

.jp-OutputPrompt {
  display: table-cell;
  vertical-align: top;
  min-width: var(--jp-cell-prompt-width);
}

body[data-format='mobile'] .jp-OutputPrompt {
  display: table-row;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
}

body[data-format='mobile'] .jp-OutputArea-child .jp-OutputArea-output {
  display: table-row;
}

.jp-OutputArea-output.jp-OutputArea-executeResult {
  width: 100%;
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }

  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}
</style>

<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
    <!-- End of mathjax configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[3]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LinearRegression</span>

<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">"housing_price_dataset.csv"</span><span class="p">)</span>

<span class="n">df</span><span class="p">[</span><span class="s1">'YearBuilt'</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'YearBuilt'</span><span class="p">],</span> <span class="nb">format</span><span class="o">=</span><span class="s1">'%Y'</span><span class="p">)</span><span class="o">.</span><span class="n">dt</span><span class="o">.</span><span class="n">year</span>

<span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int64</span><span class="p">)</span>
<span class="c1"># Remove rows with negative prices</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">]</span>

<span class="n">df</span><span class="p">[</span><span class="s1">'Bedrooms'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Bedrooms'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'Bathrooms'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Bathrooms'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'SquareFeet'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'SquareFeet'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>

<span class="c1"># Apply ordinal encoding to 'Neighborhood' column</span>
<span class="n">neighborhood_mapping</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'Rural'</span><span class="p">:</span> <span class="mi">1</span><span class="p">,</span> <span class="s1">'Suburb'</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span> <span class="s1">'Urban'</span><span class="p">:</span> <span class="mi">3</span><span class="p">}</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'Neighborhood'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Neighborhood'</span><span class="p">]</span><span class="o">.</span><span class="n">map</span><span class="p">(</span><span class="n">neighborhood_mapping</span><span class="p">)</span>

<span class="c1"># Separate features and target variable</span>
<span class="n">X</span> <span class="o">=</span> <span class="n">df</span><span class="p">[[</span><span class="s1">'Bedrooms'</span><span class="p">,</span> <span class="s1">'Bathrooms'</span><span class="p">,</span> <span class="s1">'SquareFeet'</span><span class="p">,</span> <span class="s1">'Neighborhood'</span><span class="p">,</span> <span class="s1">'YearBuilt'</span><span class="p">]]</span>
<span class="n">y</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span>

<span class="c1"># Split the data into training and testing sets for model</span>
<span class="n">X_train</span><span class="p">,</span> <span class="n">X_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">X</span><span class="p">,</span> <span class="n">y</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.2</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">17</span><span class="p">)</span>

<span class="c1"># Train the Linear Regression model</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">LinearRegression</span><span class="p">()</span>
<span class="n">model</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">X_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>

<span class="n">bedroom_multiplier</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">bathroom_multiplier</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">sf_multiplier</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">neighborhood_multiplier</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>
<span class="n">buildyear_multiplier</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">coef_</span><span class="p">[</span><span class="mi">4</span><span class="p">],</span> <span class="mi">2</span><span class="p">)</span>

<span class="k">while</span> <span class="kc">True</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">"Enter home data for an estimate. Press -1 on any answer to exit"</span><span class="p">)</span>

    <span class="n">user_bedrooms</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Number of bedrooms (between 2 and 5): "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_bedrooms</span> <span class="o">==</span> <span class="s2">"-1"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Exiting program"</span><span class="p">)</span>
        <span class="k">break</span>

    <span class="n">user_bathrooms</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Number of bathrooms (between 1 and 3): "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_bathrooms</span> <span class="o">==</span> <span class="s2">"-1"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Exiting program"</span><span class="p">)</span>
        <span class="k">break</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">user_bathrooms_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_bedrooms</span><span class="p">)</span>
    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry"</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="n">user_sf</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Home square footage (between 1000 and 2999): "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_sf</span> <span class="o">==</span> <span class="s2">"-1"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Exiting program"</span><span class="p">)</span>
        <span class="k">break</span>

    <span class="n">user_neighborhood</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Neighborhood type (1 for Rural, 2 for Suburb, 3 for Urban): "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_neighborhood</span> <span class="o">==</span> <span class="s2">"-1"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Exiting program"</span><span class="p">)</span>
        <span class="k">break</span>

    <span class="n">user_buildyear</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">"Year built (between 1950 and 2021): "</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">user_buildyear</span> <span class="o">==</span> <span class="s2">"-1"</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Exiting program"</span><span class="p">)</span>
        <span class="k">break</span>

    <span class="k">try</span><span class="p">:</span>
        <span class="n">user_bedrooms_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_bedrooms</span><span class="p">)</span>
        <span class="n">user_bathrooms_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_bathrooms</span><span class="p">)</span>
        <span class="n">user_sf_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_sf</span><span class="p">)</span>
        <span class="n">user_neighborhood_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_neighborhood</span><span class="p">)</span>
        <span class="n">user_buildyear_int</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">user_buildyear</span><span class="p">)</span>

    <span class="k">except</span> <span class="ne">ValueError</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry for one of the inputs. Please enter valid integers."</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="k">if</span> <span class="n">user_bedrooms_int</span> <span class="o">&lt;</span> <span class="mi">2</span> <span class="ow">or</span> <span class="n">user_bedrooms_int</span> <span class="o">&gt;</span> <span class="mi">5</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry. Bedrooms must be between 2 and 5"</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="k">if</span> <span class="n">user_bathrooms_int</span> <span class="o">&lt;</span> <span class="mi">1</span> <span class="ow">or</span> <span class="n">user_bathrooms_int</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry. Bedrooms must be between 1 and 3"</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="k">if</span> <span class="n">user_sf_int</span> <span class="o">&gt;</span> <span class="mi">2999</span> <span class="ow">or</span> <span class="n">user_sf_int</span> <span class="o">&lt;</span> <span class="mi">1000</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry. Square footage must be between 1000 and 2999."</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="k">if</span> <span class="n">user_neighborhood_int</span> <span class="o">&lt;</span> <span class="mi">1</span> <span class="ow">or</span> <span class="n">user_neighborhood_int</span> <span class="o">&gt;</span> <span class="mi">3</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry. Neighborhood entry must be 1, 2, oe 3."</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="k">if</span> <span class="n">user_buildyear_int</span> <span class="o">&gt;</span> <span class="mi">2021</span> <span class="ow">or</span> <span class="n">user_buildyear_int</span> <span class="o">&lt;</span> <span class="mi">1950</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">"Invalid entry. Build year must be between 1950 and 2021."</span><span class="p">)</span>
        <span class="k">continue</span>

    <span class="n">model_beds</span> <span class="o">=</span> <span class="n">user_bedrooms_int</span>
    <span class="n">model_baths</span> <span class="o">=</span> <span class="n">user_bathrooms_int</span>
    <span class="n">model_sf</span> <span class="o">=</span> <span class="n">user_sf_int</span>
    <span class="n">model_neighborhood</span> <span class="o">=</span> <span class="n">user_neighborhood_int</span>
    <span class="n">model_year</span> <span class="o">=</span> <span class="n">user_buildyear_int</span>

    <span class="n">estimate</span> <span class="o">=</span> <span class="nb">round</span><span class="p">(((</span><span class="n">model_beds</span> <span class="o">*</span> <span class="n">bedroom_multiplier</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">model_baths</span> <span class="o">*</span> <span class="n">bathroom_multiplier</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">model_sf</span> <span class="o">*</span> <span class="n">sf_multiplier</span><span class="p">)</span>
                <span class="o">+</span> <span class="p">(</span><span class="n">model_neighborhood</span> <span class="o">*</span> <span class="n">neighborhood_multiplier</span><span class="p">)</span> <span class="o">+</span> <span class="p">(</span><span class="n">model_year</span> <span class="o">*</span> <span class="n">buildyear_multiplier</span><span class="p">)))</span>

    <span class="n">currency_estimate</span> <span class="o">=</span> <span class="s2">"</span><span class="si">{:,}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">estimate</span><span class="p">)</span>

    <span class="nb">print</span><span class="p">(</span><span class="s2">"Price estimate: $"</span> <span class="o">+</span> <span class="nb">str</span><span class="p">(</span><span class="n">currency_estimate</span><span class="p">))</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>


<div class="jp-RenderedText jp-OutputArea-output" data-mime-type="text/plain">
<pre>Enter home data for an estimate. Press -1 on any answer to exit
Number of bedrooms (between 2 and 5): 2
Number of bathrooms (between 1 and 3): 2
Home square footage (between 1000 and 2999): 1852
Neighborhood type (1 for Rural, 2 for Suburb, 3 for Urban): 2
Year built (between 1950 and 2021): 1998
Price estimate: $179,606
Enter home data for an estimate. Press -1 on any answer to exit
Number of bedrooms (between 2 and 5): -1
Exiting program
</pre>
</div>
</div>

</div>

</div>

</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell   ">
<div class="jp-Cell-inputWrapper">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In&nbsp;[4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
     <div class="CodeMirror cm-s-jupyter">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>

<span class="c1"># Add the following magic command to display Matplotlib plots in the notebook</span>
<span class="o">%</span><span class="k">matplotlib</span> inline

<span class="c1"># Read the csv</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s2">"housing_price_dataset.csv"</span><span class="p">)</span>

<span class="c1"># Convert 'YearBuilt' column to datetime format</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'YearBuilt'</span><span class="p">]</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">to_datetime</span><span class="p">(</span><span class="n">df</span><span class="p">[</span><span class="s1">'YearBuilt'</span><span class="p">],</span> <span class="nb">format</span><span class="o">=</span><span class="s1">'%Y'</span><span class="p">)</span><span class="o">.</span><span class="n">dt</span><span class="o">.</span><span class="n">year</span>

<span class="c1"># Convert 'Price' column to int64</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int64</span><span class="p">)</span>
<span class="c1"># Remove rows with negative prices</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="n">df</span><span class="p">[</span><span class="s1">'Price'</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="mi">0</span><span class="p">]</span>

<span class="c1"># Convert 'SquareFeet', 'Bedrooms', and 'Bathrooms' to int32</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'Bedrooms'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Bedrooms'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'Bathrooms'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'Bathrooms'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">df</span><span class="p">[</span><span class="s1">'SquareFeet'</span><span class="p">]</span> <span class="o">=</span> <span class="n">df</span><span class="p">[</span><span class="s1">'SquareFeet'</span><span class="p">]</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>

<span class="n">mean_price_by_neighborhood</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">'Neighborhood'</span><span class="p">)[</span><span class="s1">'Price'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">mean_price_by_bedrooms</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">'Bedrooms'</span><span class="p">)[</span><span class="s1">'Price'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>
<span class="n">mean_price_by_bathrooms</span> <span class="o">=</span> <span class="n">df</span><span class="o">.</span><span class="n">groupby</span><span class="p">(</span><span class="s1">'Bathrooms'</span><span class="p">)[</span><span class="s1">'Price'</span><span class="p">]</span><span class="o">.</span><span class="n">mean</span><span class="p">()</span><span class="o">.</span><span class="n">astype</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">int32</span><span class="p">)</span>

<span class="c1"># Create subplots</span>
<span class="n">fig</span><span class="p">,</span> <span class="n">axes</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="mi">2</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">12</span><span class="p">,</span> <span class="mi">10</span><span class="p">))</span>

<span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">mean_price_by_neighborhood</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="n">mean_price_by_neighborhood</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">])</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">'Mean Price by Neighborhood'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">'Neighborhood'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">'Mean Price'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">mean_price_by_neighborhood</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">-</span> <span class="mi">5000</span><span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="n">mean_price_by_neighborhood</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">+</span> <span class="mi">5000</span><span class="p">)</span>

<span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">mean_price_by_bedrooms</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="n">mean_price_by_bedrooms</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">])</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">'Mean Price by Bedrooms'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">'Number of Bedrooms'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">'Mean Price'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">0</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">mean_price_by_bedrooms</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">-</span> <span class="mi">5000</span><span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="n">mean_price_by_bedrooms</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">+</span> <span class="mi">5000</span><span class="p">)</span>

<span class="n">sns</span><span class="o">.</span><span class="n">barplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="n">mean_price_by_bathrooms</span><span class="o">.</span><span class="n">index</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="n">mean_price_by_bathrooms</span><span class="o">.</span><span class="n">values</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">])</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">'Mean Price by Bathrooms'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_xlabel</span><span class="p">(</span><span class="s1">'Number of Bathrooms'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylabel</span><span class="p">(</span><span class="s1">'Mean Price'</span><span class="p">)</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">set_ylim</span><span class="p">(</span><span class="nb">min</span><span class="p">(</span><span class="n">mean_price_by_bathrooms</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">-</span> <span class="mi">5000</span><span class="p">,</span> <span class="nb">max</span><span class="p">(</span><span class="n">mean_price_by_bathrooms</span><span class="o">.</span><span class="n">values</span><span class="p">)</span> <span class="o">+</span> <span class="mi">5000</span><span class="p">)</span>

<span class="n">sns</span><span class="o">.</span><span class="n">regplot</span><span class="p">(</span><span class="n">x</span><span class="o">=</span><span class="s1">'SquareFeet'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'Price'</span><span class="p">,</span> <span class="n">data</span><span class="o">=</span><span class="n">df</span><span class="p">,</span> <span class="n">ax</span><span class="o">=</span><span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">],</span> <span class="n">scatter_kws</span><span class="o">=</span><span class="p">{</span><span class="s1">'s'</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span> <span class="s1">'alpha'</span><span class="p">:</span> <span class="mf">0.5</span><span class="p">})</span>
<span class="n">axes</span><span class="p">[</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">'Linear Regression: Price vs Square Feet'</span><span class="p">)</span>

<span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>

     </div>
</div>
</div>
</div>

<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>


<div class="jp-OutputArea jp-Cell-outputArea">

<div class="jp-OutputArea-child">

    
    <div class="jp-OutputPrompt jp-OutputArea-prompt"></div>




<div class="jp-RenderedImage jp-OutputArea-output ">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABKUAAAPdCAYAAABba9tpAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8pXeV/AAAACXBIWXMAAA9hAAAPYQGoP6dpAAEAAElEQVR4nOzdfVxUZf7/8fcIMiDChCgiimKZKIKa96gJZoLlTe5WrktRbC21CVqh+01r3cpK2jKtcLPNdbWU0lq1ZbX4ijdppJiCpOTtVqZ8EbXCwUgB8fz+6MfZJlDBYBB8PR+PeWxzrs85c80Zaq59z3WuYzEMwxAAAAAAAADgRM0augMAAAAAAAC4+hBKAQAAAAAAwOkIpQAAAAAAAOB0hFIAAAAAAABwOkIpAAAAAAAAOB2hFAAAAAAAAJyOUAoAAAAAAABORygFAAAAAAAApyOUAgAAAAAAgNMRSgFOtmTJElksFlksFn300UdV2g3DUJcuXWSxWBQZGen0/tVGZGSk+V4sFos8PDzUq1cvvfzyyzp//nyNjmGxWPTUU0/Vb0d/JjIyUqGhofX+OkFBQbJYLPrDH/5Qpe2jjz6SxWLRP//5z1of9/Dhw7JYLFqyZMll9ctisSgxMfGSdU899ZQsFou++eaby3qd2qh8T3PmzKn316qpyn9XDx8+3NBdAQDUAcZgjq6GMVjlw93dXV26dFFSUlKdj2sYLwC/DKEU0EC8vLy0aNGiKts3b96sL774Ql5eXg3Qq9q79tprtW3bNm3btk0rVqxQ+/bt9eijj2rGjBk12n/btm36/e9/X8+9bFiLFi3SgQMH6ux47dq107Zt2zR69Og6OyYAAFcLxmA/aupjsCFDhpjn58MPP9SDDz6ov/3tbxo1alRDdw3ATxBKAQ3kN7/5jVauXKni4mKH7YsWLVJ4eLg6duzYQD2rHQ8PDw0aNEiDBg3SuHHj9K9//UvXXnut5s+fr/Ly8mr3MQxDZ86ckSQNGjRIHTp0cGaXnSo8PFyenp56/PHH6+yYVqtVgwYNUps2bersmA3phx9+aOguAACuIozBro4x2DXXXGOen+HDh+uPf/yjpk6dquzsbB08eNDp/ak87wAcEUoBDeS3v/2tJOmdd94xt9ntdq1cuVL33XdftfuUlZXp2WefVbdu3WS1WtWmTRv97ne/08mTJx3qVqxYoaioKLVr104eHh7q3r27pk+frpKSEoe6uLg4tWzZUv/5z3906623qmXLlgoMDNTUqVNVWlp6We+refPm6tu3r3744QezX5WXi73++uvq3r27rFar3nzzTbPt51PH/+///k8PPPCAAgMD5ebmpoCAAN1xxx06fvy4WVNcXKxp06apc+fOcnNzU/v27fXII49UeY8X8/HHH2vQoEHy8PBQ+/btNXPmTFVUVEj6cdB2/fXXKzo6usp+33//vWw2mxISEi75Gq1atdL06dO1atUqZWVlXbL+0KFDiomJkZ+fn6xWq7p3766//vWvDjUXunzvX//6l3r27Cmr1aprr71Wr7zyinkJXnWWLl2q7t27q0WLFurVq5fWrFlTbd3Ro0f161//Wt7e3rLZbLr77rur/M2dP39eL7zwgvm36efnp3vuuUf5+fkOdZXT9rds2aLBgwerRYsWVf7e586dq86dO6tly5YKDw+v9rylpaUpPDxcLVq0kJeXl0aOHKlt27ZVqcvMzNSIESPk5eWlFi1aaPDgwVq7dm2VuqysLA0ZMkTu7u4KCAjQjBkzLjigBwA0bozBro4xWHVsNpukH8/VT+3cuVPjxo1Tq1at5O7urhtuuEHvvvtulf1rOl4ICgrSmDFjtGrVKt1www1yd3fX008/LUnKy8vTbbfdJh8fH7m7u6t3797mZ/JTR44c0d133+0wJnzppZccLs+sHBO++OKL+stf/qKgoCB5eHgoMjJSBw8eVHl5uaZPn66AgADZbDb96le/0okTJxxeZ+PGjYqMjJSvr688PDzUsWNH3X777fxoCOcxADjV4sWLDUnGjh07jNjYWGPAgAFm24IFCwxPT0+juLjY6NGjhxEREWG2VVRUGKNGjTI8PT2Np59+2sjIyDD+/ve/G+3btzdCQkKMH374wax95plnjHnz5hlr1641PvroI+P11183OnfubAwfPtyhL/fee6/h5uZmdO/e3ZgzZ46xfv16489//rNhsViMp59++pLvJSIiwujRo0eV7X369DFcXV3NPkky2rdvb/Ts2dN4++23jY0bNxp5eXlm25NPPmnum5+fb7Rr185o3bq1MXfuXGP9+vXGihUrjPvuu8/Yt2+fYRiGUVJSYvTu3duh5pVXXjFsNptx0003GefPn79kv319fY2AgADj1VdfNf73f//XmDJliiHJSEhIMOte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06dPKy0tzWH6+Ntvv61mzZpp2LBhDrUPP/ywoqKidO+998rFxUXx8fGX9ZqS9Je//EVDhw7Vq6++6rC9RYsWGj58uHbt2qWePXte8NfY6nh6eqpfv356//33NWfOHHPf77///oJ31KuN1NRU9e3b13z+7rvv6ty5c4qMjJQk81K8ZcuWqX///mbdjh07tG/fPj3xxBO/uA+VgoOD1b59e7399tuaNm2a+fdeUlKilStXmnfkk6SBAwdq1apVmjNnjjw8PCT9eJfAZcuWqUOHDuaU+uHDhystLU3Hjx83f72tqKjQihUr6qzfAIArD2MwR019DCZJubm5kiQ/Pz9JP44rrr/+en322WeaPXv2Rfeti/HCiBEjtHr1ahUUFJizniTprbfeUosWLTRo0CCzLjk5WTk5OerTp49DncVi0fDhw2v8mjXl4uKigQMHqlu3bkpNTVVOTg6hFJyCUAq4Ajz//POXrJk4caJSU1N166236uGHH9aAAQPUvHlz5efna9OmTbrtttv0q1/9SoMHD5aPj4/+8Ic/6Mknn1Tz5s2Vmppq/iJ0pZs1a5Y+/PBDDRs2TI8//rjCwsJ06tQppaenKykpSd26ddMjjzyilStXatiwYXr00UfVs2dPnT9/XkeOHNG6des0derUiw4apR9/gXrooYd05MgRde3aVR988IEWLlyohx56SB07dnSoHTlypEJCQrRp0ybz1ryXa8iQIbrtttv0r3/9q0rbK6+8oqFDh+rGG2/UQw89pKCgIJ0+fVr/+c9/9O9//7vK+gE/NWvWLI0ePVrR0dF6+OGHVVFRoRdffFEtW7bUd999d9n9laRVq1bJ1dVVI0eO1Oeff66ZM2eqV69emjBhgqQfB3QPPPCAUlJS1KxZM91yyy06fPiwZs6cqcDAQD366KO/6PV/qlmzZnrhhRd01113acyYMXrwwQdVWlqqF198UadOnXL4dyk5OVkjR47U8OHDNW3aNLm5uem1115TXl6e3nnnHfP/PPzpT39SWlqabrrpJv35z39WixYt9Ne//rVWt7YGADROjMH+q6mNwU6dOmWux1leXq59+/Zp9uzZslqtDrPS//a3v+mWW25RdHS04uLi1L59e3333Xfat2+fcnJy9N5770mqm/HCk08+qTVr1mj48OH685//rFatWik1NVVr167VCy+8IJvNJkl69NFH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pKVLlyozM7NOOwcAANCUMIYCAAD4r1qHUitXrlR0dLQ8PDy0a9culZaWSpJOnz6t2bNn13kHAQAAmgLGUAAAAI5qHUo9++yzev3117Vw4UI1b97c3D548GDl5OTUaecAAACaCsZQAAAAjmodSh04cEDDhg2rst3b21unTp2qiz4BAAA0OYyhAAAAHNU6lGrXrp3+85//VNmemZmpa6+9tk46BQAA0NQwhgIAAHBU61DqwQcf1MMPP6zt27fLYrGooKBAqampmjZtmiZNmlQffQQAAGj0GEMBAAA4cq3tDv/zP/8ju92u4cOH6+zZsxo2bJisVqumTZumxMTE+ugjAABAo8cYCgAAwFGtQylJeu655/TEE09o7969On/+vEJCQtSyZcu67hsAAECTwhgKAADgvy4rlJKkFi1aqF+/fnXZFwAAgCaPMRQAAMCPahxK3XfffTWq+8c//nHZnQEAAGhqGEMBAABUr8ah1JIlS9SpUyfdcMMNMgyjPvsEAADQZDCGAgAAqF6NQ6k//OEPWr58ub788kvdd999uvvuu9WqVav67BsAAECjxxgKAACges1qWvjaa6/p2LFjeuyxx/Tvf/9bgYGBmjBhgv73f/+XX/0AAAAugDEUAABA9Wq10LnVatVvf/tb/fa3v9XXX3+tJUuWaNKkSSovL9fevXu5e4yT9P3jWw3dBVxBsl+8p6G7AAC4BMZQAAAAVdV4ptTPWSwWWSwWGYah8+fP12WfAAAAmizGUAAAAD+qVShVWlqqd955RyNHjlRwcLD27Nmj+fPn68iRI5f1C19ycrL69+8vLy8v+fn5afz48Tpw4IDZXl5erscee0xhYWHy9PRUQECA7rnnHhUUFFR7PMMwdMstt8hisej99993aCsqKlJsbKxsNptsNptiY2N16tQph5ojR45o7Nix8vT0VOvWrTVlyhSVlZU51OzZs0cRERHy8PBQ+/btNWvWLKbeAwCAi6rrMRQAAEBTUOPL9yZNmqTly5erY8eO+t3vfqfly5fL19f3F7345s2blZCQoP79++vcuXN64oknFBUVpb1798rT01M//PCDcnJyNHPmTPXq1UtFRUV65JFHNG7cOO3cubPK8V5++WVZLJZqXysmJkb5+flKT0+XJD3wwAOKjY3Vv//9b0lSRUWFRo8erTZt2igzM1Pffvut7r33XhmGoZSUFElScXGxRo4cqeHDh2vHjh06ePCg4uLi5OnpqalTp/6icwEAAJqm+hhDAQAANAU1DqVef/11dezYUZ07d9bmzZu1efPmautWrVpV4xevDIgqLV68WH5+fsrOztawYcNks9mUkZHhUJOSkqIBAwboyJEj6tixo7n9s88+09y5c7Vjxw61a9fOYZ99+/YpPT1dWVlZGjhwoCRp4cKFCg8P14EDBxQcHKx169Zp7969Onr0qAICAiRJL730kuLi4vTcc8/J29tbqampOnv2rJYsWSKr1arQ0FAdPHhQc+fOVVJS0gUDMQAAcPWqjzEUAABAU1DjUOqee+6p99DFbrdL0kVvk2y322WxWHTNNdeY23744Qf99re/1fz58+Xv719ln23btslms5mBlCQNGjRINptNW7duVXBwsLZt26bQ0FAzkJKk6OholZaWKjs7W8OHD9e2bdsUEREhq9XqUDNjxgwdPnxYnTt3rvLapaWlKi0tNZ8XFxfX7GQAAIAmwRljKAAAgMaoxqHUkiVL6rEbP64HlZSUpKFDhyo0NLTamrNnz2r69OmKiYmRt7e3uf3RRx/V4MGDddttt1W7X2Fhofz8/Kps9/PzU2FhoVnTtm1bh3YfHx+5ubk51AQFBTnUVO5TWFhYbSiVnJysp59++gLvGgAANHX1PYYCAABorGocStW3xMRE7d69W5mZmdW2l5eXa+LEiTp//rxee+01c3taWpo2btyoXbt2XfT41f1CaRiGw/bLqalc5PxCv4DOmDFDSUlJ5vPi4mIFBgZetK8AAAAAAABNXa3uvldfJk+erLS0NG3atEkdOnSo0l5eXq4JEyboq6++UkZGhsMsqY0bN+qLL77QNddcI1dXV7m6/piz3X777YqMjJQk+fv76/jx41WOe/LkSXOmk7+/vzkjqlJRUZHKy8svWnPixAlJqjLLqpLVapW3t7fDAwAAAAAA4GrXoKGUYRhKTEzUqlWrtHHjxmovf6sMpA4dOqT169dXuVvN9OnTtXv3buXm5poPSZo3b54WL14sSQoPD5fdbtenn35q7rd9+3bZ7XYNHjzYrMnLy9OxY8fMmnXr1slqtapv375mzZYtW1RWVuZQExAQUOWyPgAAAAAAAFxYg16+l5CQoLffflv/+te/5OXlZc5Cstls8vDw0Llz53THHXcoJydHa9asUUVFhVnTqlUr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OnHihNleeXnqhg0b1K9fP7Vo0UKDBw9mlgbgROnp6YqLi1OPHj3Uq1cvLV68WEeOHFF2dnZDdw31YOzYsbr11lvVtWtXde3aVc8995xatmyprKyshu4a6tH333+vu+66SwsXLpSPj09Ddwf1yNXVVf7+/uajTZs2Dd2lKw6hFK4IX375pdLT02v9a/+LL76o0NBQZWdna+bMmZIkLy8vLVmyRHv37tUrr7yihQsXat68efXRbTQyLVu2VMuWLfX++++rtLT0Fx3rj3/8o+bMmaMdO3bIz89P48aNq3X4uWHDBu3bt08ZGRlas2aNuf3FF19Uz549lZOToxkzZujRRx9VRkbGL+ovmpb//Oc/evfdd7Vy5UqHEPXNN9+Uq6urtm/frldffVXz5s3T3//+d7O9rKxMzzzzjD777DO9//77+uqrrxzC/kpPPPGEXnrpJe3cuVOurq667777nPCuAFTHbrdLklq1atXAPUF9q6io0PLly1VSUqLw8PCG7g7qUUJCgkaPHq2bb765obuCenbo0CEFBASoc+fOmjhxor788suG7tIVh8v30GDWrFmjli1bqqKiQmfPnpUkzZ07t1bHuOmmmzRt2jSHbX/605/Mfw4KCtLUqVO1YsUK/c///M8v7zQaNVdXVy1ZskTx8fF6/fXX1adPH0VERGjixIm1njr95JNPauTIkZJ+DAI6dOig1atXa8KECTU+hqenp/7+979XuWxvyJAhmj59uiSpa9eu+uSTTzRv3jzz9YCysjItXbq0yq9tgYGBmjdvniwWi4KDg7Vnzx7NmzfPnEn603Dp2muv1auvvqoBAwbo+++/V8uWLc225557ThEREZKk6dOna/To0Tp79qzc3d2d8O4AVDIMQ0lJSRo6dKhCQ0MbujuoJ3v27FF4eLjOnj2rli1bavXq1QoJCWnobqGeLF++XDk5OdqxY0dDdwX1bODAgXrrrbfUtWtXHT9+XM8++6wGDx6szz//XL6+vg3dvSsGM6XQYIYPH67c3Fxt375dkydPVnR0tCZPnlyrY/Tr16/Ktn/+858aOnSo/P391bJlS82cOVNHjhypq26jkbv99ttVUFCgtLQ0RUdH66OPPlKfPn20ZMmSWh3np79gtmrVSsHBwdq3b1+tjhEWFlbtOlI//3U0PDy81sdG09apU6dqp38PGjTIYUH08PBwHTp0SBUVFZKkXbt26bbbblOnTp3k5eWlyMhISary38ifhrTt2rWTJIfL/AA4R2Jionbv3n3Z622icQgODlZubq6ysrL00EMP6d5779XevXsbuluoB0ePHtXDDz+sZcuW8UPPVeCWW27R7bffrrCwMN18881au3atpB9/0MZ/EUqhwXh6eqpLly7q2bOnXn31VZWWlurpp5+WJDVr1sxhHRRJ1V4a9fMFP7OysjRx4kTdcsstWrNmjXbt2qUnnnhCZWVl9fdG0Oi4u7tr5MiR+vOf/6ytW7cqLi5OTz75pJo1+/E/iT/926vNJXmVYcDl/v3W5Nho2ry9vc1LdX7q1KlT8vb2Np9fzmLHJSUlioqKUsuWLbVs2TLt2LFDq1evlqQq/4386aXUlX9758+fr/VrArh8kydPVlpamjZt2qQOHTo0dHdQj9zc3NSlSxf169dPycnJ6tWrl1555ZWG7hbqQXZ2tk6cOKG+ffvK1dVVrq6u2rx5s1599VW5urqaPyKhafL09FRYWJgOHTrU0F25ohBK4Yrx5JNPas6cOSooKFCbNm107Ngxs62iokJ5eXmXPMYnn3yiTp066YknnlC/fv10/fXX6+uvv67PbqMJCAkJUUlJiTnz5Kd/ez9dr+enfroAaVFRkQ4ePKhu3bpJktq0aaPCwkKHYOpCx7nUsSufVx4bTVu3bt20c+fOKtt37Nih4ODgS+5f3d/O9ddfLxcXF+3fv1/ffPONnn/+ed14443q1q0bs5+AK5BhGEpMTNSqVau0ceNGde7cuaG7BCczDOMXr32JK9OIESO0Z88e5ebmmo9+/frprrvuUm5uLndma+JKS0u1b98+cxY6fsSaUrhiREZGqkePHpo9e7ZuuukmJSUlae3atbruuus0b948nTp16pLH6NKli44cOaLly5erf//+Wrt2rTkTAPj2229155136r777lPPnj3l5eWlnTt36oUXXtBtt90mDw8PDRo0SM8//7yCgoL0zTffOKxR9lOzZs2Sr6+v2rZtqyeeeEKtW7fW+PHjJf34t3zy5Em98MILuuOOO5Senq4PP/zQYabLxXzyySd64YUXNH78eGVkZOi9994zp/uiaZs0aZLmz5+vhIQEPfDAA/Lw8FBGRoYWLVqkpUuXXnL/o0ePKikpSQ8++KBycnKUkpKil156SZLUsWNHubm5KSUlRX/4wx+Ul5enZ555pr7fEoBaSkhI0Ntvv61//etf8vLyUmFhoSTJZrPJw8OjgXuHuvb444/rlltuUWBgoE6fPq3ly5fro48+Unp6ekN3DfXAy8uryvpwnp6e8vX1Zd24JmjatGkaO3asOnbsqBMnTujZZ59VcXGx7r333obu2hWFmVK4oiQlJWnhwoW69dZbde+99+qee+5RRESEOnfurOHDh19y/9tuu02PPvqoEhMT1bt3b23dutW8Kx/QsmVLDRw4UPPmzdOwYcMUGhqqmTNnKj4+XvPnz5ck/eMf/1B5ebn69eunhx9+WM8++2y1x3r++ef18MMPq2/fvjp27JjS0tLM9aG6d++u1157TX/961/Vq1cvffrpp1UW5L+YqVOnKjs7WzfccIOeeeYZvfTSS4qOjv7lJwBXvKCgIH388cf64osvFBUVpf79+2vJkiVasmSJ7rzzzkvuf8899+jMmTMaMGCAEhISNHnyZD3wwAOSfpzBt2TJEr333nsKCQnR888/rzlz5tT3WwJQSwsWLJDdbldkZKTatWtnPlasWNHQXUM9OH78uGJjYxUcHKwRI0Zo+/btSk9P5+YmQBOQn5+v3/72twoODtavf/1rubm5KSsrS506dWrorl1RLMbPFz4BAAAAAAAA6hkzpQAAAAAAAOB0hFIAAAAAAABwOkIpAAAAAAAAOB2hFAAAAAAAAJyOUAoAAAAAAABORygFAAAAAAAApyOUAgAAAAAAgNMRSgFocoKCgvTyyy/XuP7w4cOyWCzKzc29YM2SJUt0zTXX/OK+Veepp55S79696+XYlxIZGalHHnmkQV4bAADUr5qMcZxt//79GjRokNzd3Rtk/BMXF6fx48c7/XUBVI9QCsAVIy4uThaLRc8//7zD9vfff18Wi6XGx9mxY4ceeOCBuu4eAABArdTV2KYpefLJJ+Xp6akDBw5ow4YN1dZUnrfKh6+vr0aNGqXdu3c7ubcA6huhFIAriru7u/7yl7+oqKjoso/Rpk0btWjRog57VX/Ky8sbugsAAKAe1cXY5kpTVlZ22ft+8cUXGjp0qDp16iRfX98L1o0aNUrHjh3TsWPHtGHDBrm6umrMmDGX/bo19UveG4DaI5QCcEW5+eab5e/vr+Tk5AvWbN26VcOGDZOHh4cCAwM1ZcoUlZSUmO0/v3xv//79Gjp0qNzd3RUSEqL169fLYrHo/fffdzjul19+qeHDh6tFixbq1auXtm3bVuW133//fXXt2lXu7u4a+f/Yu+84qarz8eOfO312dna2ssvS6yKC6Fc6KmIBC6AxSiIGRY2a2AWNURNFY+/+0GhiUIxiTIxijQg2ECkiUkRg6bDL9jplp9/z+2OYcYetIFWf9/e1+br3nnvvufcuzOHZ8zznzDMpKipK2v/888/Tq1cvLBYLBQUFvPrqq0n7NU3jhRde4LzzzsPhcHD//fcn9r366qt0794dl8vFr3/9azweT2JfMBjkxhtvpEOHDthsNk466SRWrFiRdO6FCxcydOhQrFYrHTt25I9//CORSCSx3+fzcemll5KamkrHjh154oknWnzGQgghhDgw2jO2aS6V/+mnn6Z79+6J7+NpZw8++CC5ubmkp6dz7733EolEuO2228jMzKRz58689NJLTc6/ceNGRo4cic1m49hjj+WLL75I2r9+/XrOOeccUlNTyc3NZcqUKVRVVSX2n3rqqVx//fVMmzaN7OxszjzzzGbvQ9d17rvvPjp37ozVauX4449n3rx5if2aprFy5Uruu+8+NE1jxowZLT4Tq9VKXl4eeXl5HH/88dx+++0UFRVRWVmZaLN7925+9atfkZGRQVZWFueddx47duxI7I9Go0ybNo309HSysrL4wx/+gFIq6Tot3Vtb46q2xmZffPEFmqbx8ccfc8IJJ2C32znttNOoqKjgo48+4phjjiEtLY2LL76YhoaGxHH//e9/GThwIHa7naysLM4444ykca4QPzUSlBJCHFGMRiMPPvggM2fOpLi4uMn+7777jnHjxnHBBRewdu1a/v3vf7N48WKuv/76Zs+n6zrnn38+KSkpLF++nL///e/cddddzba96667uPXWW1m9ejV9+/bl4osvThp8NDQ08MADD/DKK6/w1Vdf4Xa7+fWvf53YP3fuXG666SamT5/OunXruOaaa7j88sv5/PPPk65zzz33cN555/Hdd99xxRVXALHfGr7zzjt88MEHfPDBByxcuDBpqv8f/vAH3nrrLV555RW+/fZbevfuzbhx46ipqQFig7JzzjmHIUOGsGbNGp5//nlmzZqVFPS67bbb+Pzzz5k7dy7z58/niy++YOXKlW29EiGEEEL8CG2NbfbFZ599RklJCYsWLeLJJ59kxowZjB8/noyMDJYvX87vfvc7fve73zX5pdltt93G9OnTWbVqFSNHjmTixIlUV1cDUFpayujRozn++OP55ptvmDdvHuXl5UyaNCnpHK+88gomk4mvvvqKv/3tb83275lnnuGJJ57g8ccfZ+3atYwbN46JEyeyefPmxLWOPfZYpk+fTmlpKbfeemu77tvr9TJnzhx69+6dmF3V0NDAmDFjSE1NZdGiRSxevJjU1FTOOuusxGynJ554gpdeeolZs2axePFiampqmDt3bpPz731v7RlXtTU2i5sxYwbPPvssS5YsoaioiEmTJvH000/z+uuv8+GHH7JgwQJmzpyZeD4XX3wxV1xxBRs2bOCLL77gggsuaBJIE+InRQkhxBHisssuU+edd55SSqnhw4erK664Qiml1Ny5c1X8r6spU6aoq6++Oum4L7/8UhkMBuX3+5VSSnXr1k099dRTSimlPvroI2UymVRpaWmi/YIFCxSg5s6dq5RSavv27QpQ//jHPxJtvv/+ewWoDRs2KKWUevnllxWgli1blmizYcMGBajly5crpZQaOXKkuuqqq5L6dtFFF6lzzjkn8T2gbr755qQ299xzj0pJSVFutzux7bbbblPDhg1TSinl9XqV2WxWc+bMSewPhUIqPz9fPfroo0oppe68805VUFCgdF1PtHnuuedUamqqikajyuPxKIvFot54443E/urqamW329VNN92khBBCCHHgtWdso1RsLDBo0KCkY5966inVrVu3pHN169ZNRaPRxLaCggJ18sknJ76PRCLK4XCof/3rX0qpH8Y4Dz/8cKJNOBxWnTt3Vo888ohSSqk///nPauzYsUnXLioqUoAqLCxUSik1evRodfzxx7d5v/n5+eqBBx5I2jZkyBB17bXXJr4fNGiQuueee1o9z2WXXaaMRqNyOBzK4XAoQHXs2FGtXLky0WbWrFlNxj7BYFDZ7Xb18ccfK6WU6tixY7P3Hn8nLd1bW+Oq9ozNPv/8cwWoTz75JNHmoYceUoDaunVrYts111yjxo0bp5RSauXKlQpQO3bsaPX5CPFTIjOlhBBHpEceeYRXXnmF9evXJ21fuXIls2fPJjU1NfE1btw4dF1n+/btTc5TWFhIly5dyMvLS2wbOnRos9c87rjjEv/dsWNHACoqKhLbTCYTgwcPTnzfr18/0tPT2bBhAwAbNmxg1KhRSeccNWpUYn9c43PEde/eHafTmXT9+LW3bt1KOBxOOrfZbGbo0KFJ1x4xYkRS0dRRo0bh9XopLi5m69athEIhRowYkdifmZlJQUFBs89CCCGEEAdWS2ObfXHsscdiMPzwT7jc3FwGDhyY+N5oNJKVlZU0fgGSPv/j45n4GGLlypV8/vnnSWOrfv36AbExSFxz45fG3G43JSUl7RoLtceYMWNYvXo1q1evZvny5YwdO5azzz6bnTt3Jvq9ZcsWnE5not+ZmZkEAgG2bt1KfX09paWlzd773vbe1p5xVVtjs7jG48vc3FxSUlLo2bNn0rb4+xo0aBCnn346AwcO5KKLLuLFF1/8SdUiE6I5psPdASGEaM4pp5zCuHHjuPPOO5k6dWpiu67rXHPNNdx4441NjunatWuTbUqpdq9uYzabE/8dP0bX9aQ2zZ2r8ba99zd3fYfD0eq14+eJX1vtmbLd2rmbu07j45RM+xZCCCEOq5bGNgAGg6HJZ3Vzi6E0N15obQzRmsZjnQkTJvDII480aRP/JR00P35p7bxx+zIWa8zhcNC7d+/E9yeeeCIul4sXX3yR+++/H13XOfHEE5kzZ06TY3Nycvb5Wm31ublxVXvude/xZWvvy2g0smDBApYsWcL8+fOZOXMmd911F8uXL6dHjx77dE9CHC1kppQQ4oj18MMP8/7777NkyZLEtv/7v//j+++/p3fv3k2+LBZLk3P069ePXbt2UV5enti2d4Hw9opEInzzzTeJ7wsLC6mrq0v8NvGYY45h8eLFSccsWbKEY445Zr+uFxe/t8bnDofDfPPNN4lz9+/fnyVLliQNaJcsWYLT6aRTp0707t0bs9nMsmXLEvtra2vZtGnTj+qbEEIIIdqvubENxIIoZWVlSZ/jq1evPmDXbfz5H4lEWLlyZWL8Eh9bde/evcnYqr2BKIC0tDTy8/MPylgIYsEbg8GA3+9P9Hvz5s106NChSb9dLhcul4uOHTs2e+9tac+4qq2x2Y+5z1GjRnHvvfeyatUqLBZLs3WwhPipkKCUEOKINXDgQC655JJE8UeA22+/naVLl3LdddexevVqNm/ezHvvvccNN9zQ7DnOPPNMevXqxWWXXcbatWv56quvEoXO9/W3dmazmRtuuIHly5fz7bffcvnllzN8+PBEOuBtt93G7NmzeeGFF9i8eTNPPvkkb7/9druLeLbE4XDw+9//nttuu4158+axfv16rrrqKhoaGrjyyisBuPbaaykqKuKGG25g48aNvPvuu9xzzz1MmzYNg8FAamoqV155Jbfddhuffvop69atY+rUqUkpAEIIIYQ4uJob20BsBbjKykoeffRRtm7dynPPPcdHH310wK773HPPMXfuXDZu3Mh1111HbW1tYrGV6667jpqaGi6++GK+/vprtm3bxvz587niiiuIRqP7dJ3bbruNRx55hH//+98UFhbyxz/+kdWrV3PTTTftc5+DwSBlZWWUlZWxYcMGbrjhBrxeLxMmTADgkksuITs7m/POO48vv/yS7du3s3DhQm666aZEQfmbbrqJhx9+OHHv1157LXV1dW1eu61xVXvGZvtj+fLlPPjgg3zzzTfs2rWLt99+m8rKygMS1BPiSCXpe0KII9pf/vIX/vOf/yS+P+6441i4cCF33XUXJ598MkopevXqxa9+9atmjzcajbzzzjv89re/ZciQIfTs2ZPHHnuMCRMmYLPZ9qkvKSkp3H777UyePJni4mJOOumkpGWXzz//fJ555hkee+wxbrzxRnr06MHLL7/Mqaeeul/33tjDDz+MrutMmTIFj8fD4MGD+fjjj8nIyACgU6dO/O9//+O2225j0KBBZGZmcuWVV/KnP/0pcY7HHnsMr9fLxIkTcTqdTJ8+nfr6+h/dNyGEEEK0395jG4jNtv7rX//Kgw8+yF/+8hd++ctfcuutt/L3v//9gFzz4Ycf5pFHHmHVqlX06tWLd999l+zsbADy8/P56quvuP322xk3bhzBYJBu3bpx1lln7fMvr2688UbcbjfTp0+noqKC/v37895779GnT5997vO8efMS6YNOp5N+/frx5ptvJsZVKSkpLFq0iNtvv50LLrgAj8dDp06dOP3000lLSwNIrPIX/0XcFVdcwS9+8Ys2xz/tGVe1NTbbH2lpaSxatIinn34at9tNt27deOKJJzj77LP3+5xCHOk0JYVGhBA/M1999RUnnXQSW7ZsoVevXoe7O0IIIYQQQgjxsyRBKSHET97cuXNJTU2lT58+bNmyhZtuuomMjIwmNQ+EEEIIIYQQQhw6kr4nhPjJ83g8/OEPf6CoqIjs7GzOOOMMnnjiicPdLSGEEEIIIYT4WZOZUkIIIYQQQgghhBDikJNll4QQQgghhBBCCCHEISdBKSGEEEIIIYQQQghxyElQSgghhBBCCCGEEEIcchKUEkIIIYQQQgghhBCHnASlhBBCCCGEEEIIIcQhJ0EpIYQQQgghhBBCCHHISVBKCCGEEEIIIYQQQhxyEpQSQgghhBBCCCGEEIecBKWEEEIIIYQQQgghxCEnQSkhhBBCCCGEEEIIcchJUEoIIYQQQgghhBBCHHISlBJCCCGEEEIIIYQQh5wEpYQQQgghhBBCCCHEISdBKSGEEEIIIYQQQghxyElQSoijxOzZs9E0DU3T+OKLL5rsV0rRu3dvNE3j1FNPPeT92xennnpq4l40TcNutzNo0CCefvppdF1v1zk0TWPGjBkHt6N7OfXUUxkwYMBBv0737t2Tno/NZqN3795MmzaNqqqq/Trn+vXrmTFjBjt27Giy71DdlxBCiCNHfFzxzTfftNhmx44daJrG7NmzD13HDqAvvvgi6fPUaDSSk5PDhAkTWr3vn5r4u25uDHC4NH4vmqbhcrk49dRT+fDDD9t1fPzdNjcmPppVV1dzxx130L9/fxwOBy6Xi379+jFlyhTWrl17uLt3UMX/vmnua/DgwQflmg0NDcyYMeMn93N0tDEd7g4IIfaN0+lk1qxZTQJPCxcuZOvWrTidzsPTsX3Us2dP5syZA0BFRQUvvPACt9xyC6WlpTzyyCNtHr906VI6d+58sLt52IwaNYrHH38cAL/fzzfffMOMGTNYtGjRfg2k169fz7333supp55K9+7dD3BvhRBC/BR17NiRpUuX0qtXr8PdlR/lwQcfZMyYMYTDYVatWsW9997L6NGjWb16NX369Dnc3Tvozj33XJYuXUrHjh0Pd1eSXHjhhUyfPh1d19m2bRv3338/EyZM4P333+fcc89t9dj/+7//Y+nSpfTv3/8Q9fbg83q9DB8+HK/Xy2233cagQYPw+/1s2rSJt99+m9WrV3Pccccd7m4edDfccAOTJ09O2paamnpQrtXQ0MC9994LcMT/Uv+nTIJSQhxlfvWrXzFnzhyee+450tLSEttnzZrFiBEjcLvdh7F37We32xk+fHji+7PPPpt+/frx7LPPcv/992M2m5sco5QiEAg0OfanKD09Pekex4wZg8fj4S9/+QubNm2ib9++h7F3PwiHw2iahskkHydCCPFTY7Vaj/jP24aGBlJSUlpt06dPn8R9nHzyyaSnp3PZZZfx2muvJf5Beqi0p78HWk5ODjk5OYf0mu2Rm5ubeC8jR45kxIgR9O7dm6effrrFoFR83JGWlnbE/2zuqzfffJMtW7bw2WefMWbMmKR906ZNa3c2weFwIMeDXbt2/cm9W9E6Sd8T4ihz8cUXA/Cvf/0rsa2+vp633nqLK664otljQqEQ999/P/369cNqtZKTk8Pll19OZWVlUrt///vfjB07lo4dO2K32znmmGP44x//iM/nS2o3depUUlNT2bJlC+eccw6pqal06dKF6dOnEwwG9+u+zGYzJ554Ig0NDYl+aZrG9ddfzwsvvMAxxxyD1WrllVdeSezbO31v9+7dXH311XTp0gWLxUJ+fj4XXngh5eXliTZut5tbb72VHj16YLFY6NSpEzfffHOTe2zNl19+yfDhw7Hb7XTq1Ik///nPRKNRIBY469OnD+PGjWtynNfrxeVycd111+3r4wHA5XIBJAXsvvnmG37961/TvXt37HY73bt35+KLL2bnzp2JNrNnz+aiiy4CYsGt+FTovdMxVqxYwcknn0xKSgo9e/bk4YcfThoAxafKv/rqq0yfPp1OnTphtVrZsmULAC+99BKDBg3CZrORmZnJL37xCzZs2NDkPt577z1GjBhBSkoKTqeTM888k6VLlya1mTFjBpqmsXbtWi666CJcLheZmZlMmzaNSCRCYWEhZ511Fk6nk+7du/Poo48mHa/rOvfffz8FBQXY7XbS09M57rjjeOaZZ/bjyQshxM9Tc+l78b+fv//+ey6++GJcLhe5ublcccUV1NfXJx2vlOKvf/0rxx9/PHa7nYyMDC688EK2bduW1G7BggWcd955dO7cOZGyfs011zRJWY9f+9tvv+XCCy8kIyNjv2ZxxVOBGo8PADZv3szkyZPp0KEDVquVY445hueee67J8d9//z1jx44lJSWFnJwcrrvuOj788MMm6WTx9PhFixYxcuRIUlJSEmO19o5H3nzzTYYNG4bL5Up8Pjce77Xn866l9L32fG4fjDFfS3r16kVOTk5iDNPauKOl9L3ly5czYcIEsrKysNls9OrVi5tvvjmpTXvf895OOOEETj755Cbbo9EonTp14oILLkhse/755xk0aBCpqak4nU769evHnXfe2er5q6urAVqc0WYwJP/T/cMPP+T444/HarXSo0cPHn/88cSfkbjWUnD3Hktv2bKFyy+/nD59+pCSkkKnTp2YMGEC3333XdJxbY0HP/nkE04//XTS0tJISUlh1KhRfPrpp63e+7745ptvmDhxIpmZmdhsNk444QT+85//NGlXVlbGNddcQ+fOnbFYLPTo0YN7772XSCSSeDbxYO29996bGB9PnTr1gPVVtI8EpYQ4yqSlpXHhhRfy0ksvJbb961//wmAw8Ktf/apJe13XOe+883j44YeZPHkyH374IQ8//DALFizg1FNPxe/3J9pu3ryZc845h1mzZjFv3jxuvvlm/vOf/zBhwoQm5w2Hw0ycOJHTTz+dd999lyuuuIKnnnqqXal3Ldm6dSsmk4mMjIzEtnfeeYfnn3+eu+++m48//rjZwQDEAlJDhgxh7ty5TJs2jY8++oinn34al8tFbW0tEPvt5OjRo3nllVe48cYb+eijj7j99tuZPXs2EydORCnVZh/Lysr49a9/zSWXXMK7777LhRdeyP33389NN90ExD7gb7jhBhYsWMDmzZuTjv3nP/+J2+1uV1BKKUUkEiESieD1evn88895+umnGTVqFD169Ei027FjBwUFBTz99NN8/PHHPPLII5SWljJkyJDEYP7cc8/lwQcfBOC5555j6dKlLF26NOm3kGVlZVxyySX85je/4b333uPss8/mjjvu4LXXXmvStzvuuINdu3bxwgsv8P7779OhQwceeughrrzySo499ljefvttnnnmGdauXcuIESOSnsPrr7/OeeedR1paGv/617+YNWsWtbW1nHrqqSxevLjJtSZNmsSgQYN46623uOqqq3jqqae45ZZbOP/88zn33HOZO3cup512Grfffjtvv/124rhHH32UGTNmcPHFF/Phhx/y73//myuvvJK6uro2n70QQoi2/fKXv6Rv37689dZb/PGPf+T111/nlltuSWpzzTXXcPPNN3PGGWfwzjvv8Ne//pXvv/+ekSNHJgWEtm7dyogRI3j++eeZP38+d999N8uXL+ekk04iHA43ufYFF1xA7969efPNN3nhhRf2ue/bt28HSJp1vH79eoYMGcK6det44okn+OCDDzj33HO58cYbk2ZTlZaWMnr0aAoLC3n++ef55z//icfj4frrr2/2WqWlpfzmN79h8uTJ/O9//+Paa69t93hk6dKl/OpXv6Jnz5688cYbfPjhh9x9992Jf1TD/n/etfdzG9o/5ps6deqPql1VW1tLdXV1k1ldzY07mhMfJ+7atYsnn3ySjz76iD/96U9JP2vtfc/Nufzyy1m8eHGT5zN//nxKSkq4/PLLAXjjjTe49tprGT16NHPnzuWdd97hlltuafMXoCNGjADg0ksv5Z133kkEqZrz6aefct555+F0OnnjjTd47LHH+M9//sPLL7/c6jVaU1JSQlZWFg8//DDz5s3jueeew2QyMWzYMAoLC5u0b+69vPbaa4wdO5a0tDReeeUV/vOf/5CZmcm4cePaHZjSdT0xBo5/xf9MfP7554waNYq6ujpeeOEF3n33XY4//nh+9atfJQXeysrKGDp0KB9//DF33303H330EVdeeSUPPfQQV111FRAL/s2bNw+AK6+8MjE+/vOf/7zfz1DsJyWEOCq8/PLLClArVqxQn3/+uQLUunXrlFJKDRkyRE2dOlUppdSxxx6rRo8enTjuX//6lwLUW2+9lXS+FStWKED99a9/bfZ6uq6rcDisFi5cqAC1Zs2axL7LLrtMAeo///lP0jHnnHOOKigoaPNeRo8erY499lgVDodVOBxWJSUl6o9//KMC1EUXXZRoByiXy6VqamqanANQ99xzT+L7K664QpnNZrV+/foWr/vQQw8pg8GgVqxYkbT9v//9rwLU//73vzb7Dah33303aftVV12lDAaD2rlzp1JKKbfbrZxOp7rpppuS2vXv31+NGTOm1WsopVS3bt0U0ORr6NChqrS0tNVjI5GI8nq9yuFwqGeeeSax/c0331SA+vzzz1u8r+XLlzfp77hx4xLfx3/uTjnllKR2tbW1ym63q3POOSdp+65du5TValWTJ09WSikVjUZVfn6+GjhwoIpGo4l2Ho9HdejQQY0cOTKx7Z577lGAeuKJJ5LOefzxxytAvf3224lt4XBY5eTkqAsuuCCxbfz48er4449v8TkJIcTPXeNxRUu2b9+uAPXyyy8ntsX/fn700UeT2l577bXKZrMpXdeVUkotXbq02b/Hi4qKlN1uV3/4wx+avWZ8/LFz584mn7nxa999993tusf459a///1vFQ6HVUNDg/rqq69UQUGB6t+/v6qtrU20HTdunOrcubOqr69POsf111+vbDZbYixy2223KU3T1Pfff5/Ubty4cU0+Z+Ofr59++mlS2/aORx5//HEFqLq6uhbvsT2fd/F3vX37dqVU+z+3ldq3Md8VV1yhjEaj2rFjR6v9USo2jrv22mtVOBxWoVBIbdiwQZ199tkKUM8995xSquVxR+N9jZ93r169VK9evZTf72/xuu19z82pqqpSFotF3XnnnUnbJ02apHJzc1U4HE6cKz09vc1n0Jz77rtPWSyWxNivR48e6ne/+13SOFwppYYNG6by8/OT7tXtdqvMzEzV+J/4zf0Zjtt7LL23SCSiQqGQ6tOnj7rlllsS21t6Lz6fT2VmZqoJEyYkbY9Go2rQoEFq6NChrd57vK/NfS1YsEAppVS/fv3UCSeckHjWcePHj1cdO3ZMjC+vueYalZqamhibx8X/TMX//FZWVrb5HMTBJzOlhDgKjR49ml69evHSSy/x3XffsWLFihZT9z744APS09OZMGFC0m8cjj/+ePLy8pKmPW/bto3JkyeTl5eH0WjEbDYzevRogCbTuTVNazKD6rjjjktKG2vN999/j9lsxmw2k5+fzxNPPMEll1zCiy++mNTutNNOS5o51ZKPPvqIMWPGcMwxx7TY5oMPPmDAgAEcf/zxSc9i3Lhx7V7Bxel0MnHixKRtkydPRtd1Fi1alGhz+eWXM3v27MRvxT777DPWr1/f4m9S93bSSSexYsUKVqxYwVdffcWsWbOorKzktNNOS0pn8Hq93H777fTu3RuTyYTJZCI1NRWfz9ds6lxL8vLyGDp0aNK2lt7nL3/5y6Tvly5dit/vbzLduUuXLpx22mmJ34wVFhZSUlLClClTkqagp6am8stf/pJly5bR0NCQdI7x48cnfX/MMcegaRpnn312YpvJZKJ3795JfR06dChr1qzh2muv5eOPPz5qaq0JIcTRYu/PwuOOO45AIEBFRQUQ+8zVNI3f/OY3SZ+5eXl5DBo0KOkzt6Kigt/97nd06dIFk8mE2WymW7duQNPxBzT9HGrLr371K8xmcyKVyO128+GHH5Keng5AIBDg008/5Re/+AUpKSlJ/T3nnHMIBAIsW7YMiC0sM2DAgCYFtuPlFfaWkZHBaaedlrStveORIUOGALFZw//5z3/YvXt3k/Pvz+ddez+349o75ps1axaRSCTx7try17/+FbPZjMVi4ZhjjmHJkiXcd999XHvttUnt2vO+N23axNatW7nyyiux2WzNttmX99ycrKwsJkyYwCuvvJIob1BbW8u7777LpZdemqinNHToUOrq6rj44ot5991392nl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bR577LFE4Mnj8fD+++8nHZubm4vNZkvMMop79913m1xf07Qmz+3DDz9k9+7d9O7du+WHsseoUaNIT0/fp3IV+6KgoIA+ffqwZs2aJoGzvY0fP57//e9/9OrVq9VfeB7M8bFoPwlKCXEUe/jhh9ts8+tf/5o5c+ZwzjnncNNNNzF06FDMZjPFxcV8/vnnnHfeefziF79g5MiRZGRk8Lvf/Y577rkHs9nMnDlzErNyjnT33XcfH330Eaeccgp33nknAwcOpK6ujnnz5jFt2jT69evHzTffzFtvvcUpp5zCLbfcwnHHHYeu6+zatYv58+czffr0VgN3EPvt4u9//3t27dpF3759+d///seLL77I73//e7p27ZrU9swzz6R///58/vnn/OY3v2lxtZjm1NXVJeoahMNhNmzYwIMPPojVak38di8tLY1TTjmFxx57jOzsbLp3787ChQuZNWtWk99oDRgwAIC///3vOJ3ORMpkc2l7+yo9PZ0///nP3HnnnVx66aVcfPHFVFdXc++992Kz2bjnnnuA2FLGjz76KJdccgnjx4/nmmuuIRgM8thjj1FXV9eun+f2mjBhAgMGDGDw4MGJ5aWffvppunXrRp8+fQ7YdYQQ4mj32WefNbta2jnnnPOjzjtq1CiuvvpqLr/8cr755htOOeUUHA4HpaWlLF68mIEDB/L73/+efv360atXL/74xz+ilCIzM5P333+/SQrZgWQ2m3nwwQeZNGkSzzzzDH/605945plnOOmkkzj55JP5/e9/T/fu3fF4PGzZsoX333+fzz77DICbb76Zl156ibPPPpv77ruP3NxcXn/9dTZu3AjQJKDQnPaOR+6++26Ki4s5/fTT6dy5M3V1dTzzzDNJNT/35/OuvZ/b++rKK6/klVdeYevWrfs8G+hAeO6555gwYQLDhw/nlltuoWvXruzatYuPP/6YOXPmALT7Pbfmiiuu4JFHHmHy5MnY7fYmq19fddVV2O12Ro0aRceOHSkrK+Ohhx7C5XIl6oQ159VXX+Vvf/sbkydPZsiQIbhcLoqLi/nHP/7B999/z913350IpP3lL3/hrLPO4swzz2T69OlEo1EeeeQRHA5H0mz5eF23l156iV69ejFo0CC+/vprXn/99SbXHz9+PLNnz6Zfv34cd9xxrFy5kscee6zN8hhxqampzJw5k8suu4yamhouvPBCOnToQGVlJWvWrKGyspLnn3++Xedqyd/+9jfOPvtsxo0bx9SpU+nUqRM1NTVs2LCBb7/9ljfffBOI/btgwYIFjBw5khtvvJGCggICgQA7duzgf//7Hy+88AKdO3fG6XTSrVs33n33XU4//XQyMzMTY2pxCB3mQutCiHZqzyo5SjVdfU+p2Opkjz/+uBo0aJCy2WwqNTVV9evXT11zzTVq8+bNiXZLlixRI0aMUCkpKSonJ0f99re/Vd9++22TVTsuu+wy5XA4mlw7vipOW+Kr77UFUNddd12L+/ZeKaOoqEhdccUVKi8vT5nNZpWfn68mTZqkysvLE228Xq/605/+pAoKCpTFYlEul0sNHDhQ3XLLLaqsrKxd/f7iiy/U4MGDldVqVR07dlR33nlnk1VA4mbMmKEAtWzZsjbvN27v1feMRqPq2rWruvDCC9WqVauS2hYXF6tf/vKXKiMjQzmdTnXWWWepdevWqW7duqnLLrssqe3TTz+tevTooYxGY9I7bel9XHbZZapbt26J7+Orrbz55pvN9vsf//iHOu644xLP9bzzzmuyOpFSSr3zzjtq2LBhymazKYfDoU4//XT11VdfJbWJ/yxVVlY26VNzP3t738MTTzyhRo4cqbKzs5XFYlFdu3ZVV155ZbtWBBJCiJ+D+Liipa/t27e3uvre3n8/773CW9xLL72khg0bphwOh7Lb7apXr17q0ksvVd98802izfr169WZZ56pnE6nysjIUBdddJHatWtXk8/6lq7dkrY+t4YNG6YyMjISq9tt375dXXHFFapTp07KbDarnJwcNXLkSHX//fcnHbdu3Tp1xhlnKJvNpjIzM9WVV16pXnnllSarFbc23mnPeOSDDz5QZ599turUqZOyWCyqQ4cO6pxzzlFffvll4jzt+bxr6d2053N7X8Z88ZX69r5Oc1ob48W19v6aW31Pqdiqj2effbZyuVzKarWqXr16Ja0cp1T733NrRo4cqQB1ySWXNNn3yiuvqDFjxqjc3FxlsVgS49G1a9e2es7169er6dOnq8GDB6ucnBxlMplURkaGGj16tHr11VebtH/vvfcS769r167q4Ycfbva91NfXq9/+9rcqNzdXORwONWHCBLVjx44mf75qa2vVlVdeqTp06KBSUlLUSSedpL788ks1evTopH9btPXnauHChercc89VmZmZ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OFg2b95Mfn4+PXr04Ne//jXbtm0DYPv27ZSVlTF27NhEW6vVyujRoxMlC1auXEk4HE5qk5+fz4ABA5LKGhyu0gcQSy90u91JX0IIIYT46TmsQSmlFNdffz1vv/02n332GT169Gj3cXsXDx87diwWi4X33nsPm82W1H7EiBHU19fz9ddfJ7YtX76c+vp6Ro4cmWizbt06SktLE23mz5+P1WrlxBNPTLRZtGhRUq2E+fPnk5+fT/fu3ff5/oUQQggh9tWwYcP45z//yccff8yLL75IWVkZI0eOpLq6OvHLs+bKDTQuR2CxWMjIyGi1zeEqfQBSk1MIIYT4uTisQanrrruO1157jddffx2n00lZWRllZWX4/X4AfD4fd955J8uWLWPnzp18++23/Pa3v6W4uJiLLroIiM2QGjt2LD6fj1mzZuF2uxPniddFOOaYYzjrrLO46qqrWLZsGcuWLeOqq65i/PjxFBQUADB27Fj69+/PlClTWLVqFZ9++im33norV111VaJS/OTJk7FarUydOpV169Yxd+5cHnzwQZl+LoQQQohD5uyzz+aXv/wlAwcO5IwzzuDDDz8EYml6cc2VG2hrrHIgyhq0p01bpQ9AanIKIYQQPxeHNSj1/PPPU19fz6mnnkrHjh0TX//+978BMBqNbNy4kV/+8pf07duX8ePHU1lZyZdffsmxxx4LxKagL1++nO+++47evXsnnafxAGbOnDkMHDiQsWPHMnbsWI477jheffXVxH6j0ciHH36IzWZj1KhRTJo0ifPPP5/HH3880cblcrFgwQKKi4sZPHgw1157LdOmTWPatGmH6IkJIYQQQiRzOBwMHDiQzZs3J+pMNVduoHE5glAoRG1tbattDmfpA6vVSlpaWtKXEEIIIX56Dmuh87aWA7bZbLz99tuttjn11FPbtaxwZmYmr732WqttunbtygcffNBqm4EDB7Jo0aI2ryeEEEIIcSgEg0E2bNjAySefTI8ePcjLy2PBggWccMIJAIRCIRYuXMgjjzwCwIknnojZbGbBggVMmjQJgNLSUtatW8ejjz4KJJc+GDp0KNB86YMHHniA0tJSOnbsCDRf+uDOO+8kFAphsVgSbaT0gRBCCCHgCCl0LoQQQggh2ufWW29l4cKFbN++neXLl3PhhRfidru57LLL0DSNm2++mQcffJC5c+eybt06pk6d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PF4Y85nPfIbHH3+cRx99lJdeeolEIsHVV1+NZVmFMTfccAObN2/m6aef5umnn2bz5s2sXLnymJ8fHPocU6kUGzdu5O6772bjxo385je/YdeuXVx77bVDxt588820trYWvn784x8XPT9e5ziW+7urrrqq6Nj/8Ic/FD1/In+Go53fwPNqbW3lv/7rv9A0jfe9731F407Uz28s90In83U42vmd7NfgWO9lT+ZrcCzneDJfh6Pd+53w158S4iQFqMcff3y8D0OIIh0dHQpQL7zwwngfihAFZWVl6j/+4z/G+zCEOOYG3xvYtq1qa2vVfffdV3gsk8mocDisfvSjHymllIpEIsrlcqlHH320MKa5uVnpuq6efvpppZRS27ZtU4Bat25dYczatWsVoHbs2HGMz6rYWO5/1q9frwB18ODBwmOXXHKJ+sd//McRtzlRznG487vpppvUddddN+I2J9NnOJbP77rrrlOXX3550WMny+en1NB7oVPtOhzLvd7JfA0Od36n0jWo1Ng+w5P9Ouy/9zsZrj+plBJCiKMoGo0CUF5ePs5HIgRYlsWjjz5KMplk6dKl4304Qhx3+/fvp62tjSuvvLLwmMfj4ZJLLuHll18GYMOGDRiGUTSmrq6O+fPnF8asXbuWcDjM4sWLC2OWLFlCOBwujDmRRKNRNE2jtLS06PFHHnmEyspKzjzzTD772c8W/ZX8RD/Hv/zlL1RXVzN79mxuvvlmOjo6Cs+dSp9he3s7Tz31FB/72MeGPHeyfH6D74VOtetwLPd6J/M1ONL5nUrX4Gif4cl8HQ6+9zsZrj/n29paCCFEgVKKO+64g4suuoj58+eP9+GI09jrr7/O0qVLyWQylJSU8PjjjzNv3rzxPiwhjru2tjYAampqih6vqanh4MGDhTFut5uysrIhY/q3b2tro7q6esj+q6urC2NOFJlMhi984QvccMMNhEKhwuM33ngj06ZNo7a2ljfeeIO77rqLLVu2sHr1auDEPsd3vetdfOADH2DKlCns37+fu+++m8svv5wNGzbg8XhOqc/wZz/7GcFgkPe+971Fj58sn99w90Kn0nU4lnu9k/kaHOn8TqVrcCyf4cl4HY5079cfGJ3I15+EUkIIcZTceuutbN26lZdeemm8D0Wc5ubMmcPmzZuJRCL8+te/5qabbuKFF16QYEqctjRNK/peKTXkscEGjxlu/Fj2czwZhsGHP/xhbNvmhz/8YdFzN998c+Gf58+fz6xZszj//PPZuHEj5557LnDinuOHPvShwj/Pnz+f888/nylTpvDUU08N+aVxoJPxM/yv//ovbrzxRrxeb9HjJ8vnd6h7oVPhOhztXu9kvwZHOr9T6Rocy/36yXgdjnTv1+9Evv5k+p4QQhwFt912G08++STPP/889fX143044jTndruZOXMm559/Pvfeey8LFy7k3/7t38b7sIQ47mprawGG/BW3o6Oj8Ffj2tpacrkcvb29hxzT3t4+ZP+dnZ1D/vo8XgzD4IMf/CD79+9n9erVRRUawzn33HNxuVzs3r0bODnOsd+ECROYMmVK0bGfCp/hiy++yM6dO/n4xz8+6tgT8fMb6V7oVLkOR7vXO9mvwcO5lz1Zr8GxnOPJeh2OdO93Mlx/EkoJIcTboJTi1ltv5Te/+Q3PPfcc06ZNG+9DEmIIpRTZbHa8D0OI465/mkX/1AqAXC7HCy+8wLJlywA477zzcLlcRWNaW1t54403CmOWLl1KNBpl/fr1hTGvvPIK0Wi0MGY89f8yvHv3bp555hkqKipG3ebNN9/EMAwmTJgAnPjnOFB3dzeNjY2FYz8VPkOA//zP/+S8885j4cKFo449kT6/0e6FTvbrcCz3eifzNXgk97In2zV4OOd4sl6Hg/Xf+50U19/bapMuxHEWj8fVpk2b1KZNmxSgHnjgAbVp06ailS2EOJ4+9alPqXA4rP7yl7+o1tbWwlcqlRrvQxOnqbvuukutWbNG7d+/X23dulV98YtfVLquqz//+c/jfWhCHBOj3Rvcd999KhwOq9/85jfq9ddfVx/5yEfUhAkTVCwWK+zjk5/8pKqvr1fPPPOM2rhxo7r88svVwoULlWmahTFXXXWVOuuss9TatWvV2rVr1YIFC9TVV1897udoGIa69tprVX19vdq8eXPRf4uy2axSSqk9e/aoe+65R7366qtq//796qmnnlJnnHGGOuecc06IczzU+cXjcXXnnXeql19+We3fv189//zzaunSpWrixIknzWc4lvvXaDSq/H6/euihh4Zsf6J/fmO5FzqZr8PRzu9kvwZHO79T4Roc6/36yXodjnbvd6JffxJKiZPK888/r4AhXzfddNN4H5o4TQ338wion/70p+N9aOI09dGPflRNmTJFud1uVVVVpd7xjndIICVOaaPdG9i2rb761a+q2tpa5fF41PLly9Xrr79etI90Oq1uvfVWVV5ernw+n7r66qtVQ0ND0Zju7m514403qmAwqILBoLrxxhtVb2/vuJ/j/v37R/xv0fPPP6+UUqqhoUEtX75clZeXK7fbrWbMmKFuv/121d3dfUKc46HOL5VKqSuvvFJVVVUpl8ulJk+erG666aYhn8+J/BmO5f71xz/+sfL5fCoSiQzZ/kT//MZyL3QyX4ejnd/Jfg2Odn6nwjU41vv1k/U6HO3e70S//jSllDryOishhBBCCCGEEEIIIQ6f9JQSQgghhBBCCCGEEMedhFJCCCGEEEIIIYQQ4riTUEoIIYQQQgghhBBCHHcSSgkhhBBCCCGEEEKI405CKSGEEEIIIYQQQghx3EkoJYQQQgghhBBCCCGOOwmlhBBCCCGEEEIIIcRxJ6GUEEIIIYQQQgghhDjuJJQSQpywDhw4gKZpbN68ebwPpWDHjh0sWbIEr9fL2WefPS7HoGkaTzzxxLi8thBCCCGEEEIcLRJKCSFGtGrVKjRN47777it6/IknnkDTtHE6qvH11a9+lUAgwM6dO3n22WeHHdP/vvV/VVRUcNVVV7F169bDeq2vfe1r4xZ8CSGEEOLU09HRwT/8wz8wefJkPB4PtbW1rFixgrVr1473oY3J4Hus/q89e/Yclf3LvZcQx5+EUkKIQ/J6vdx///309vaO96EcNblc7oi33bt3LxdddBFTpkyhoqJixHFXXXUVra2ttLa28uyzz+J0Orn66quP+HXfDqUUpmmOy2sLIYQQ4sTxvve9jy1btvCzn/2MXbt28eSTT3LppZfS09Mzrsd1OPdmA++x+r+mTZt2DI9OCHEsSSglhDikd77zndTW1nLvvfeOOGa4vyp973vfY+rUqYXvV61axfXXX883v/lNampqKC0t5Z577sE0TT73uc9RXl5OfX09//Vf/zVk/zt27GDZsmV4vV7OPPNM/vKXvxQ9v23bNt797ndTUlJCTU0NK1eupKurq/D8pZdeyq233sodd9xBZWUlV1xxxbDnYds2X//616mvr8fj8XD22Wfz9NNPF57XNI0NGzbw9a9/HU3T+NrXvjbie9L/18fa2lrOPvtsPv/5z9PY2EhnZ2dhzOc//3lmz56N3+9n+vTp3H333RiGAcDDDz/MPffcw5YtWwp/BXz44YcL23Z1dfE3f/M3+P1+Zs2axZNPPll47i9/+QuapvGnP/2J888/H4/Hw4svvkg2m+X222+nuroar9fLRRddxKuvvlp03C+88AKLFi3C4/EwYcIEvvCFLxQFWpdeeim33XYbn/nMZygrK6OmpoZ///d/J5lM8vd///cEg0FmzJjBH//4x8I2vb293HjjjVRVVeHz+Zg1axY//elPR3zvhBBCCHH0RSIRXnrpJe6//34uu+wypkyZwqJFi7jrrrt4z3veA8Du3btZvnw5Xq+XefPmsXr16qK2Af33GJFIpLDfzZs3o2kaBw4cAKC7u5uPfOQj1NfX4/f7WbBgAb/85S+LjmWke7PR7umg+B6r/8vhcADwu9/9jvPOOw+v18v06dML95r9otEon/jEJ6iuriYUCnH55ZezZcsWYPR7LyHEsSGhlBDikBwOB9/85jd58MEHaWpqelv7eu6552hpaWHNmjU88MADfO1rX+Pqq6+mrKyMV155hU9+8pN88pOfpLGxsWi7z33uc9x5551s2rSJZcuWce2119Ld3Q1Aa2srl1xyCWeffTavvfYaTz/9NO3t7Xzwgx8s2sfPfvYznE4nf/3rX/nxj3887PH927/9G9/5znf49re/zdatW1mxYgXXXnstu3fvLrzWmWeeyZ133klrayuf/exnx3TeiUSCRx55hJkzZxZVVwWDQR5++GG2bdvGv/3bv/GTn/yE7373uwB86EMf4s477+TMM88s/BXwQx/6UGHbe+65hw9+8INs3bqVd7/73dx4441D/sr5z//8z9x7771s376ds846i3/+53/m17/+NT/72c/YuHEjM2fOZMWKFYXtmpubefe7380FF1zAli1beOihh/jP//xP/uVf/mXIe1lZWcn69eu57bbb+NSnPsUHPvABli1bxsaNG1mxYgUrV64klUoBcPfdd7Nt2zb++Mc/sn37dh566CEqKyvH9N4JIYQQ4ugoKSmhpKSEJ554gmw2O+R527Z573vfi8PhYN26dfzoRz/i85///GG/TiaT4bzzzuP3v/89b7zxBp/4xCdYuXIlr7zyStG4wfdmY72nG8mf/vQn/vZv/5bbb7+dbdu28eMf/5iHH36Yb3zjG0C+cvw973kPbW1t/OEPf2DDhg2ce+65vOMd76Cnp2fUey8hxDGihBBiBDfddJO67rrrlFJKLVmyRH30ox9VSin1+OOPq4H/+vjqV7+qFi5cWLTtd7/7XTVlypSifU2ZMkVZllV4bM6cOeriiy8ufG+apgoEAuqXv/ylUkqp/fv3K0Ddd999hTGGYaj6+np1//33K6WUuvvuu9WVV15Z9NqNjY0KUDt37lRKKXXJJZeos88+e9TzraurU9/4xjeKHrvgggvUpz/96cL3CxcuVF/96lcPuZ+bbrpJORwOFQgEVCAQUICaMGGC2rBhwyG3+9a3vqXOO++8wvfDva9KKQWoL3/5y4XvE4mE0jRN/fGPf1RKKfX8888rQD3xxBNFY1wul3rkkUcKj+VyOVVXV6e+9a1vKaWU+uIXv6jmzJmjbNsujPnBD36gSkpKCp/bJZdcoi666KLC8/2f2cqVKwuPtba2KkCtXbtWKaXUNddco/7+7//+kOcuhBBCiGPvscceU2VlZcrr9aply5apu+66S23ZskUppdSf/vQn5XA4VGNjY2H8H//4RwWoxx9/XCn11j1Gb29vYcymTZsUoPbv3z/i67773e9Wd955Z+H74e7NxnJPN/geKxAIqPe///1KKaUuvvhi9c1vfrNo+//5n/9REyZMUEop9eyzz6pQKKQymUzRmBkzZqgf//jHSqmR772EEMeOc5yyMCHESeb+++/n8ssv58477zzifZx55pno+lsFmjU1NcyfP7/wvcPhoKKigo6OjqLtli5dWvhnp9PJ+eefz/bt2wHYsGEDzz//PCUlJUNeb+/evcyePRuA888//5DHFovFaGlp4cILLyx6/MILLyyUdR+Oyy67jIceegiAnp4efvjDH/Kud72L9evXM2XKFAAee+wxvve977Fnzx4SiQSmaRIKhca0/7POOqvwz4FAgGAwOOR9G3jOe/fuxTCMovNzuVwsWrSo8F5u376dpUuXFjWxv/DCC0kkEjQ1NTF58uQhr93/mS1YsKDwWE1NDUDheD71qU/xvve9j40bN3LllVdy/fXXs2zZsjGdpxBCCCGOnve973285z3v4cUXX2Tt2rU8/fTTfOtb3+I//uM/iEajTJ48mfr6+sL4gfdgY2VZFvfddx+/+tWvaG5uJpvNks1mCQQCReMG35uN9Z5u4D0WUNjvhg0bePXVVwuVUf3HkslkSKVSbNiwgUQiMaQnaDqdZu/evYd9nkKIo0NCKSHEmCxfvpwVK1bwxS9+kVWrVhU9p+s6Sqmix/p7Iw3kcrmKvtc0bdjHbNse9Xj6gxPbtrnmmmu4//77h4yZMGFC4Z8H3wiNtt9+SqkjWmkwEAgwc+bMwvfnnXce4XCYn/zkJ/zLv/wL69at48Mf/jD33HMPK1asIBwO8+ijj/Kd73xnTPsfy/s28Jz7P59Dnd9w5zrcdqN9jgM/G4B3vetdHDx4kKeeeopnnnmGd7zjHdxyyy18+9vfHtO5CiGEEOLo8Xq9XHHFFVxxxRV85Stf4eMf/zhf/epX+ad/+qchYwffF/T/cXHgfd/ge77vfOc7fPe73+V73/seCxYsIBAI8JnPfGZIM/PB92aHc0838B5r4Pb33HMP733ve4c9Z9u2mTBhwpDepAClpaVDHhNCHB8SSgkhxuy+++7j7LPPLvylql9VVRVtbW1FocbmzZuP2uuuW7eO5cuXA2CaJhs2bODWW28F4Nxzz+XXv/41U6dOxek88n+lhUIh6urqeOmllwqvBfDyyy+zaNGit3cC5G/qdF0nnU4D8Ne//pUpU6bwpS99qTDm4MGDRdu43W4sy3rbrw0wc+ZM3G43L730EjfccAOQv4l87bXX+MxnPgPAvHnz+PWvf130Ob788ssEg0EmTpz4tl6/qqqKVatWsWrVKi6++GI+97nPSSglhBBCnADmzZvHE088wbx582hoaKClpYW6ujoA1q5dWzS2qqoKyPfZLCsrA4be87344otcd911/O3f/i2QD4t2797N3LlzD3kcb/ee7txzz2Xnzp3DBlb9z7e1teF0OosW4xnoaN57CSHGRhqdCyHGbMGCBdx44408+OCDRY9feumldHZ28q1vfYu9e/fygx/8oGj1tbfrBz/4AY8//jg7duzglltuobe3l49+9KMA3HLLLfT09PCRj3yE9evXs2/fPv785z/z0Y9+9LBvKj73uc9x//3386tf/YqdO3fyhS98gc2bN/OP//iPh33M2WyWtrY22tra2L59O7fddhuJRIJrrrkGyIdEDQ0NPProo+zdu5f/9//+H48//njRPqZOncr+/fvZvHkzXV1dwzYlHatAIMCnPvUpPve5z/H000+zbds2br75ZlKpFB/72McA+PSnP01jYyO33XYbO3bs4Le//S1f/epXueOOO4qmXR6ur3zlK/z2t79lz549vPnmm/z+978f9cZUCCGEEEdXd3c3l19+OT//+c/ZunUr+/fv5//+7//41re+xXXXXcc73/lO5syZw9/93d+xZcsWXnzxxaI/nkH+/mXSpEl87WtfY9euXTz11FNDqrxnzpzJ6tWrefnll9m+fTv/8A//QFtb26jH93bv6b7yla/w3//933zta1/jzTffZPv27fzqV7/iy1/+MpBfUXrp0qVcf/31/OlPf+LAgQO8/PLLfPnLX+a1114Dju69lxBibCSUEkIclv/v//v/hkzVmzt3Lj/84Q/5wQ9+wMKFC1m/fv2YV6Ybi/vuu4/777+fhQsX8uKLL/Lb3/62sHpbXV0df/3rX7EsixUrVjB//nz+8R//kXA4fNhByu23386dd97JnXfeyYIFC3j66ad58sknmTVr1mEf89NPP82ECROYMGECixcv5tVXX+X//u//uPTSSwG47rrr+Kd/+iduvfVWzj77bF5++WXuvvvuon28733v46qrruKyyy6jqqpqyHLKh+u+++7jfe97HytXruTcc89lz549/OlPfyr8pXPixIn84Q9/YP369SxcuJBPfvKTfOxjHyvczB0pt9vNXXfdxVlnncXy5ctxOBw8+uijb2ufQgghhDg8JSUlLF68mO9+97ssX76c+fPnc/fdd3PzzTfz/e9/H13Xefzxx8lmsyxatIiPf/zjRf2ZID+F/5e//CU7duxg4cKF3H///UNW6b377rs599xzWbFiBZdeeim1tbVcf/31ox7f272nW7FiBb///e9ZvXo1F1xwAUuWLOGBBx4o9PLUNI0//OEPLF++nI9+9KPMnj2bD3/4wxw4cKDQD/No33sJIUanqcG/XQohhBBCCCGEEOTDnMcff3xMwZIQQhwuqZQSQgghhBBCCCGEEMedhFJCCCGEEEIIIYQQ4riT1feEEEIIIYQQQgxLur0IIY4lqZQSQgghhBBCCCGEEMedhFJCCCGEEEIIIYQQ4riTUEoIIYQQQgghhBBCHHcSSgkhhBBCCCGEEEKI405CKSGEEEIIIYQQQghx3EkoJYQQQgghhBBCCCGOOwmlhBBCCCGEEEIIIcRxJ6GUEEIIIYQQQgghhDju/n+lnnF73163mwAAAABJRU5ErkJggg=="
class="
"
>
</div>

</div>

</div>

</div>

</div>
</body>







</html>
