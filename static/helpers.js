$(document).ready(function(){
	console.log("Document is ready!");
});

function loadButtons(button_type){
	if (button_type === 'apoptosis'){
		$("#parent").empty();
		$("#parent").append('Apoptosis refers to programmed cell death that occurs during normal, controlled mitotic growth and development. A hallmark of cancer is the ability of cells to evade this phenomenon.');
	}
	else if (button_type === 'mitosis'){
		$("#parent").empty();
		$("#parent").append('Mitosis is cell division that results in the production of two daughter cells, both identical to the parent cell. Rapidly growing tumors are characterized by excessive mitotic division.');
	}
	else if (button_type === 'lumen'){
		$("#parent").empty();
		$("#parent").append('The lumen is the central cavity of a tubular or hollow cell structure, commonly found in colonies of tumors or cancers.');
	}
	else if (button_type === 'nonlumen'){
		$("#parent").empty();
		$("#parent").append('The non-lumen is the space outside of a hollow tubular structure.');
	}
	else if (button_type === 'tumor'){
		$("#parent").empty();
		$("#parent").append('Tumors are abnormal growths of tissue that can result in <br> benign (non-spreading) or malignant symptoms.');
	}
	else if (button_type === 'nontumor'){
		$("#parent").empty();
		$("#parent").append('Non-tumorous, soft cells do not spread to other areas of the body and <br> are classified as benign.');
	}
}