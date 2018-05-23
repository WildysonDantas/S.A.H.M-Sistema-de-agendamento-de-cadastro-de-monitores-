
function radioControler(){
	var x = $('input:radio[name=radios]:checked').val();
	if(x == 1){
		document.getElementById('cpf').innerHTML = "CPF";
	
	}else{
		document.getElementById('cpf').innerHTML = "CNPJ";
	}
}

$(document).ready(function(){
		
		document.getElementById('radios-0').style.display = "none";
		document.getElementById('radios-1').style.display = "none";
		document.getElementById('pf').style.display = "none";
		document.getElementById('pj').style.display = "none";
});

function selectControler(){
	var x = $("#selectbasic option:selected").val();
	
	if(x == 1){
		$('#group *').prop('disabled', false);
		document.getElementById('cpf').innerHTML = "CPF";
		document.getElementById('radios-0').style.display = "none";
		document.getElementById('radios-1').style.display = "none";
		document.getElementById('pf').style.display = "none";
		document.getElementById('pj').style.display = "none";
		
		document.getElementById('group').style.display = "block";


	}else{
		
		document.getElementById('radios-0').style.display = "block";
		document.getElementById('radios-1').style.display = "block";
		document.getElementById('pf').style.display = "block";
		document.getElementById('pj').style.display = "block";
		//document.getElementById('group').style.display = "none";
		$('#group').hide();
		$('#group *').prop('disabled', true);		/*$("#estado").prop('disabled', true);
		$("#nome_do_banco").prop('disabled', true);
		$("#cidade").prop('disabled', true);
		$("#conta").prop('disabled', true);
		$("#endereco").prop('disabled', true);
		$("#agencia").prop('disabled', true);*/
		
	}
	
}

