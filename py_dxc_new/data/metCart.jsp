<%@ page language="java" import="java.util.*" pageEncoding="utf-8"%>
<%@include file="public.jsp"%>
<%
String path = request.getContextPath();
String basePath = request.getScheme()+"://"+request.getServerName()+":"+request.getServerPort()+path+"/";
ArrayList list=query("select id,id||':'||customized_card_id from users order by to_number(substr(id,2)) desc");
%>
<html>
<head>
	<meta http-equiv="x-ua-compatible" content="IE=edge">
	<title>MetabolicCart</title>
	<link rel="stylesheet" type="text/css" href="./css/themes/default/easyui.css">
	<link rel="stylesheet" type="text/css" href="./css/themes/icon.css">
	<link rel="stylesheet" type="text/css" href="./css/demo.css">
	<script type="text/javascript" src="./js/jquery.min.js"></script>
	<script type="text/javascript" src="./js/jquery.easyui.min.js"></script>
	<script type="text/javascript" src="./js/jquery.easyui.mobile.js"></script>
	<script type="text/javascript" src="./js/easyui-lang-zh_CN.js"></script>
  <script language="Javascript">
	var BMC_W = 200.8; // 骨矿物质含量
	var SKEL_MUSCLE_W = 0.0;    // 骨骼肌
	var SKEL_MUS_SMOOTH_IN_W = 0.0; // 骨骼肌肉量
	var WEIGHT_W = -15.69;  //体重
	var AGE_W = -2.753; // 年龄

	var MINE_CONTENT_W = -206.6; //矿物质含量
	var U_ARM_NO_FAT_PERIMETER_W = -79.59; //上臂无脂肪周长

	var TRUNK_MUSCLE_W = 98.9; // 躯干肌肉量
	var BODY_FAT_W = -0.0141;    // 体脂肪
	var L_U_ARM_PERIMETER_W = 38.75; //左上臂周长

	var PROTEIN_W = -21.32; //蛋白质
	var EXTRA_CELL_FLUID_W = 62.94; //细胞外液

	var L_U_LIMB_MUSCLE_W = -69.5; //左上肢肌肉量
	var R_U_ARM_PERIMETER_W = -16.39; //右上臂周长

	var R_D_LIMB_MUSCLE_W = -15.22; // 右下肢肌肉量

	var OBESE_GRAD_W = -5.497; //肥胖程度
	var BMI_W = 62.72; //身体质量参数
	var BODY_WATER_CONTENT_W = 0.0; //身体水分含量
	var BELLY_LINE_W = -0.3651; // 腹围
	var VISCERAL_FAT_AREA_W = 1.386; // 内脏脂肪区域
	var reserve1 = 0.0; // 保留1
	var BMR_W = 0.0; // 基础代谢率

	var INTRA_CELL_FLUID_W = 60.8; // 细胞内液
	var WEIGHT_NO_FAT_W =0.0; // 去脂体重
	var R_U_LIMB_MUSCLE_W = -349.5; //右上肢肌肉量
	var L_D_LIMB_MUSCLE_W = -44.56; //左下肢肌肉量
	var reserve2_W = 0.0; //保留2
	var reserve3_W = 0.0; //保留3
  </script>
</head>
<body>
	<!--<h2>健康指标采集</h2>	-->

	<div style="margin:20px 0;"></div>
<table align="center">
<tr>
	<td>
	<div class="easyui-panel" title="代谢车指标计算" style="width:100%;padding:10px;" >
		<div style="padding:10px 60px 20px 60px">
	    <form id="ff" method="get" action="metCartSave.jsp" target="ifrmOption">
	    	<fieldset style="border:2px red groove">
	       <legend>基本信息和指标</legend>
	    	 <table cellpadding="5" style="font-size:12px">
	    		  <tr><td>姓名(NAME):</td><td><input class="easyui-textbox" type="text" name="NAME" id="NAME" value="" ></input></td></tr>
	    		  <tr><td>年龄(AGE):</td><td><input class="easyui-numberbox" type="text" name="AGE" id="AGE" value="0" max="200" min="0" maxlength="3" data-options="required:true,prompt:'0～200'"></input></td></tr>
	    		  <tr><td>体重(WEIGHT):</td><td><input class="easyui-numberbox" type="text" name="WEIGHT"  id="WEIGHT" value="0"  precision="2" data-options="required:true"></input></td></tr>
	    		  <tr><td>去脂体重(WEIGHT_NO_FAT):</td><td><input class="easyui-numberbox" type="text" name="WEIGHT_NO_FAT"  id="WEIGHT_NO_FAT" value="0"  precision="2" data-options="required:true"></input></td></tr>
	    		  <tr><td>腹围(BELLY_LINE):</td><td><input class="easyui-numberbox" type="text" name="BELLY_LINE"   id="BELLY_LINE" value="0"    precision="2" data-options="required:true"></input></td></tr>
	    		  <tr><td>身体质量参数(BMI):</td><td><input class="easyui-numberbox" type="text" name="BMI"   id="BMI" value="0"  precision="2" data-options="required:true"></input></td></tr>
	    		  <tr><td>基础代谢率(BMR):</td><td><input class="easyui-numberbox" type="text" name="BMR"   id="BMR" value="0"  precision="2" data-options="required:true"></input></td></tr>
         </table>
        </fieldset>
       <fieldset style="border:2px red groove">
        <legend>肢体周长</legend>
        <table cellpadding="5" style="font-size:12px">
          <tr><td>上臂无脂肪周长(U_ARM_NO_FAT_PERIMETER)</td><td><input class="easyui-numberbox" type="text" name="U_ARM_NO_FAT_PERIMETER"    id="U_ARM_NO_FAT_PERIMETER"  value="0"  precision="2"  data-options="required:true"></input></td></tr>
          <tr><td>左上臂周长(L_U_ARM_PERIMETER):</td><td><input class="easyui-numberbox" type="text" name="L_U_ARM_PERIMETER" id="L_U_ARM_PERIMETER" value="0"  precision="2" data-options="required:true"></input></td></tr>
          <tr><td>右上臂周长(R_U_ARM_PERIMETER):</td><td><input class="easyui-numberbox" type="text" name="R_U_ARM_PERIMETER" id="R_U_ARM_PERIMETER" value="0"  precision="2" data-options="required:true"></input></td></tr>
        </table>
       </fieldset>
       <fieldset style="border:2px red groove">
        <legend>脂肪</legend>
        <table cellpadding="5" style="font-size:12px">
         <tr><td>体脂肪(1):  </td><td><input class="easyui-numberbox" type="text" name="BODY_FAT"  id="BODY_FAT" value="0" precision="2" data-options="required:true"></input></td></tr>
         <tr><td>内脏脂肪区域(VISCERAL_FAT_AREA):  </td><td><input class="easyui-numberbox" type="text" name="VISCERAL_FAT_AREA"  id="VISCERAL_FAT_AREA" value="0" precision="2"  data-options="required:true"></input></td></tr>
         <tr><td>肥胖程度(OBESE_GRAD):</td><td><input class="easyui-numberbox" type="text" name="OBESE_GRAD"   id="OBESE_GRAD"  value="0"  precision="2" data-options="required:true"> </input>%</td></tr>
        </table>
       </fieldset>
       <fieldset style="border:2px red groove">
        <legend>肌肉量</legend>
        <table cellpadding="5" style="font-size:12px">
        <tr><td>骨骼肌(SKEL_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="SKEL_MUSCLE"   id="SKEL_MUSCLE" value="0"  precision="2" data-options="required:true"></input></td></tr>
        <tr><td>骨骼肌肉量(包括平滑肌)(SKEL_MUS_SMOOTH_IN):</td><td><input class="easyui-numberbox" type="text" name="SKEL_MUS_SMOOTH_IN"   id="SKEL_MUS_SMOOTH_IN" value="0"  precision="2" data-options="required:true"></input></td></tr>
         <tr><td>躯干肌肉量(TRUNK_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="TRUNK_MUSCLE"   id="TRUNK_MUSCLE" value="0"  precision="2" data-options="required:true"></input></td></tr>
         <tr><td>左上肢肌肉量(L_U_LIMB_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="L_U_LIMB_MUSCLE"  id="L_U_LIMB_MUSCLE" value="0" precision="2" data-options="required:true"></input></td></tr>
         <tr><td>右上肢肌肉量(R_U_LIMB_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="R_U_LIMB_MUSCLE"  id="R_U_LIMB_MUSCLE" value="0" precision="2" data-options="required:true"></input></td></tr>
         <tr><td>左下肢肌肉量(L_D_LIMB_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="L_D_LIMB_MUSCLE"  id="L_D_LIMB_MUSCLE" value="0" precision="2" data-options="required:true"></input></td></tr>
         <tr><td>右下肢肌肉量(R_D_LIMB_MUSCLE):</td><td><input class="easyui-numberbox" type="text" name="R_D_LIMB_MUSCLE"  id="R_D_LIMB_MUSCLE" value="0" precision="2" data-options="required:true"></input></td></tr>
        </table>
       </fieldset>
       <fieldset style="border:2px red groove">
        <legend>成分及细胞液</legend>
        <table cellpadding="5" style="font-size:12px">
         <tr><td>矿物质含量(MINE_CONTENT): </td><td><input class="easyui-numberbox" type="text" name="MINE_CONTENT"  id="MINE_CONTENT"  value="0"     precision="2" data-options="required:true"></input>%</td></tr>
         <tr><td>骨矿物质含量(BMC):</td><td><input class="easyui-numberbox" type="text" name="BMC"  id="BMC"  value="0"     precision="2" data-options="required:true"></input>%</td></tr>
         <tr><td>蛋白质(PROTEIN):    </td><td><input class="easyui-numberbox" type="text" name="PROTEIN"   id="PROTEIN"   value="0"     precision="2" data-options="required:true"></input>%</td></tr>
         <tr><td>细胞内液(INTRA_CELL_FLUID):</td><td><input class="easyui-numberbox" type="text" name="INTRA_CELL_FLUID" id="INTRA_CELL_FLUID" value="0"     precision="2"  data-options="required:true"></input></td></tr>
         <tr><td>细胞外液(EXTRA_CELL_FLUID):</td><td><input class="easyui-numberbox" type="text" name="EXTRA_CELL_FLUID" id="EXTRA_CELL_FLUID" value="0"     precision="2"  data-options="required:true"></input></td></tr>
         <tr><td>身体水分含量(BODY_WATER_CONTENT):</td><td><input class="easyui-numberbox" type="text" name="BODY_WATER_CONTENT" id="BODY_WATER_CONTENT" value="0"     precision="2"  data-options="required:true"></input></td></tr>
        </table>
       </fieldset>
       <fieldset style="border:2px red groove">
        <legend>测量值和计算值</legend>
        <table cellpadding="5" style="font-size:12px">
         <tr><td>测量值(MEASURE_VALUE):</td><td><input class="easyui-numberbox" type="text" name="MEASURE_VALUE"   id="MEASURE_VALUE"   value="0"     precision="2"  data-options="prompt:'0～300'"></input></td></tr>
         <tr><td>计算值(CALC_VALUE):</td><td><input class="easyui-numberbox" type="text" name="CALC_VALUE"   id="CALC_VALUE"   value="0"     precision="2"  data-options="required:true"></input></td></tr>
         <tr><td>误差(ERROR):</td><td><input class="easyui-numberbox" type="text" name="ERROR"   id="ERROR"   value="0"     precision="2"  data-options="required:true"></input></td></tr>
        </table>
	    </form>
	    <div style="text-align:center;padding:5px">
	    	<a href="javascript:void(0)" class="easyui-linkbutton" onClick="doCalc();">计算</a>
	    	<a href="javascript:void(0)" class="easyui-linkbutton" onClick="doSubmit();">保存</a>
	    	<a href="javascript:void(0)" class="easyui-linkbutton" onClick="window.location.reload();">新建</a>
	    	<a href="javascript:void(0)" class="easyui-linkbutton" onClick="window.close();">关闭</a>

	    </div>
	  </div>
	</div>
</td></tr>
</table>
<iframe id="ifrmOption" name="ifrmOption" width="0" height="0" src=""></iframe>
<!--<iframe id="ifrmOption" name="ifrmOption" width="0" height="0" src=""></iframe>-->
	<script>
		function doCalc(){
			var CALC_VALUE=339.1 + document.getElementById("AGE").value * AGE_W
          +document.getElementById("BMR").value * BMR_W
          +document.getElementById("BMC").value * BMC_W
          +document.getElementById("OBESE_GRAD").value * OBESE_GRAD_W
          +document.getElementById("VISCERAL_FAT_AREA").value * VISCERAL_FAT_AREA_W
          +document.getElementById("SKEL_MUSCLE").value * SKEL_MUSCLE_W
          +document.getElementById("BMI").value * BMI_W
          +document.getElementById("R_U_LIMB_MUSCLE").value * R_U_LIMB_MUSCLE_W
          +document.getElementById("L_U_LIMB_MUSCLE").value * L_U_LIMB_MUSCLE_W
          +document.getElementById("TRUNK_MUSCLE").value * TRUNK_MUSCLE_W
          +document.getElementById("R_D_LIMB_MUSCLE").value * R_D_LIMB_MUSCLE_W
          +document.getElementById("L_D_LIMB_MUSCLE").value * L_D_LIMB_MUSCLE_W
          +document.getElementById("BELLY_LINE").value * BELLY_LINE_W
          +document.getElementById("R_U_ARM_PERIMETER").value * R_U_ARM_PERIMETER_W
          +document.getElementById("L_U_ARM_PERIMETER").value * L_U_ARM_PERIMETER_W
          +document.getElementById("U_ARM_NO_FAT_PERIMETER").value * U_ARM_NO_FAT_PERIMETER_W
          +document.getElementById("INTRA_CELL_FLUID").value * INTRA_CELL_FLUID_W
          +document.getElementById("EXTRA_CELL_FLUID").value * EXTRA_CELL_FLUID_W
          +document.getElementById("PROTEIN").value * PROTEIN_W
          +document.getElementById("MINE_CONTENT").value * MINE_CONTENT_W
          +document.getElementById("BODY_FAT").value * BODY_FAT_W
          +document.getElementById("BODY_WATER_CONTENT").value * BODY_WATER_CONTENT_W
          +document.getElementById("SKEL_MUS_SMOOTH_IN").value * SKEL_MUS_SMOOTH_IN_W
          +document.getElementById("WEIGHT_NO_FAT").value * WEIGHT_NO_FAT_W
          +document.getElementById("WEIGHT").value * WEIGHT_W;

      $('#CALC_VALUE').numberbox('setValue', CALC_VALUE);
      if (document.getElementById("MEASURE_VALUE").value!='0.00') $('#ERROR').numberbox('setValue', (CALC_VALUE-document.getElementById("MEASURE_VALUE").value)/document.getElementById("MEASURE_VALUE").value);
		}
		function doSubmit(){
			//document.getElementById("name").value=339.1 ;
			//document.getElementById("CALC_VALUE").value=339.1 + document.getElementById("AGE").value * AGE_W;
			doCalc();
			document.forms[0].submit();
		}
		function clearForm(){
			$('#ff').form('clear');
		}
	</script>
</body>
</html>