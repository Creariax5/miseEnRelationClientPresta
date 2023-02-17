ETH_update()

function change_buy() {
  const box = document.querySelector(".change_box")
  box.innerHTML = `<div>
                <div class="change_btn" onclick="change_buy()" id="buy_select"><div class="auto">Acheter</div></div>
                <div class="change_btn" onclick="change_sell()" id="sell"><div class="auto">Vendre</div></div>
            </div>
                <div class="auto_box">
                    <div class="inp_h">
                        <div class="inp">
                            <div class="column_val">
                                <p class="text">dépenser</p>
                                <input class="val" type="number" id="usd_price" onchange="ETH_update()" step="1" name="nb" value="10" min="0" max="100000">
                            </div>
                            <div class="right">USD</div>
                        </div>
                    </div>
                    <div>
                        <div class="inp">
                            <div class="column_val">
                                <p class="text">recevoir</p>
                                <input class="val" type="number" id="eth_price" onchange="USD_update()" step="0.0001" name="nb" value="0.0000" min="0" max="100000">
                            </div>
                            <div class="right">ETH</div>
                        </div>
                    </div>
                </div>
                <div class="auto_box">
                    <div class="text" id="ratio">1 ETH = {{ price }} USD</div>
                        <div class="pay_mode">
                                <!-- <p class="text w">Mode de paiement</p>
                                <select id="p_mod" onchange="address_update()">
                                    <option value="none">-- select --</option>
                                    <option value="paypal">PayPal</option>
                                    <option value="coin">Coins</option>
                                </select> -->
                            <div class="adr">
                                <input type="text" id="my_adr" onchange="address_update()" required="">
                                <label>ETH address</label>
                            </div>
                        </div>
                    <div id="transact_btn">
                        <button id="transact" class="import_button" onclick="paypal_redirect()">Transact</button>
                    </div>
                </div>
            </div>`;

            const txt = document.querySelector("#pr_txt")
            txt.innerHTML = `<p class="i4">Swaple, the bridge between crypto and real world ! </p>
                <br><br><br>
                <p class="i3">How to buy crypto:</p>
                <ul class="i4">
                    <li class="i4">Tu n'est pas obligé, mais il est conseillé de te <a href="#" class="a_lit">connecter</a> à ton compte Swaple. En le faisant tu auras access à l'historique de tes transactions.</li>
                    <li class="i4">Choisis le montant de la transaction. Et entre l'<a href="#" class="a_lit">adresse</a> de la crypto choisi (Pour l'instant seul ETH est supporté).</li>
                    <li class="i4">BRAVO ! Tu devrais recevoir ta crypto dans quelques secondes.</li>
                </ul>`;
  ETH_update()
}

function change_sell() {
  const box = document.querySelector(".change_box")
  box.innerHTML = `<div>
                <div class="change_btn" onclick="change_buy()" id="buy"><div class="auto">Acheter</div></div>
                <div class="change_btn" onclick="change_sell()" id="sell_select"><div class="auto">Vendre</div></div>
            </div>
            <div>
                <div class="auto_box">
                    <div class="inp_h">
                        <div class="inp">
                            <div class="column_val">
                                <p class="text">dépenser</p>
                                <input class="val" type="number" id="eth_price" onchange="USD_update()" step="0.0001" name="nb" value="0.01" min="0" max="100000">
                            </div>
                            <div class="right">ETH</div>
                        </div>
                    </div>
                    <div>
                        <div class="inp">
                        <div class="column_val">
                            <p class="text">recevoir</p>
                            <input class="val" type="number" id="usd_price" onchange="ETH_update()" step="1" name="nb" value="0" min="0" max="100000">
                        </div>
                        <div class="right">USD</div>
                        </div>
                    </div>
                </div>
                <div class="auto_box">
                    <div class="text" id="ratio">1 ETH = {{ price }} USD</div>
                    <div class="pay_mode">
                        <!-- <p class="text w">Mode de paiement</p>
                        <select id="p_mod" onchange="address_update()">
                            <option value="none">-- select --</option>
                            <option value="paypal">PayPal</option>
                            <option value="coin">Coins</option>
                        </select> -->
                        <!-- <div class="adr">
                            <input type="text" id="my_adr" onchange="address_update()" required="">
                            <label>ETH address</label>
                        </div>
                        <div class="adr">
                            <input type="text" id="key" onchange="address_update()" required="">
                            <label>secret key</label>
                        </div> -->
                        <div class="adr">
                            <input type="text" id="email" onchange="address_update()" required="">
                            <label>PayPal email</label>
                        </div>
                    </div>
                    <div id="transact_btn">
                        <button id="transact" class="import_button" onclick="paypal_to_eth_redirect()">Transact</button>
                    </div>
                </div>
            </div>`;

            const txt = document.querySelector("#pr_txt")
            txt.innerHTML = `<p class="i4">Swaple, the bridge between crypto and real world ! </p>
                <br><br><br>
                <p class="i3">How to sell crypto:</p>
                <ul class="i4">
                    <li class="i4">Tu n'est pas obligé, mais il est conseillé de te <a href="#" class="a_lit">connecter</a> à ton compte Swaple. En le faisant tu auras access à l'historique de tes transactions.</li>
                    <li class="i4">Choisis le montant de la transaction. Et entre l'<a href="#" class="a_lit">adresse</a> et la <a href="#" class="a_lit">clé secrète</a> de la crypto choisi. Puis ton <a href="#" class="a_lit">email</a> PayPal.</li>
                    <li class="i4">BRAVO ! Tu vas recevoir tes dollars sur PayPal dans quelques secondes.</li>
                </ul>`;
  USD_update()
}

function ETH_update() {
    let usd = document.getElementById("usd_price").value;
    let eth = usd / {{ price }};
    eth = eth.toFixed(5)
    document.getElementById("eth_price").value = eth;
}

function USD_update() {
    let eth = document.getElementById("eth_price").value;
    let usd = eth * {{ price }};
    usd = usd.toFixed(2)
    document.getElementById("usd_price").value = usd;
}

function address_update() {
    var inp = "paypal" //document.querySelector("#p_mod").value;
    const box = document.querySelector("#transact_btn")
    // box.innerHTML = "<button  onclick=" + "paypal_redirect()" + " class=" + "transact" + " id=" + inp + ">" + inp + "</button>" + `<div id="paypal-button-container"></div>`;
}

function paypal_redirect() {
    let usd = document.getElementById("usd_price").value;
    let address = document.querySelector("#my_adr").value;
    console.log(address);
    var inp = "paypal" //document.querySelector("#p_mod").value;
    if(inp == "paypal"){
        window.location.href = 'paypal/' + usd*100 + '/' + address;
    }
}

function login_redirect() {
    window.location.href = '/login/';
}

function my_profile_redirect() {
    window.location.href = '/profile/';
}

function paypal_to_eth_redirect() {
    let eth = document.getElementById("eth_price").value;
    let address = document.getElementById("my_adr").value;
    let key = document.getElementById("key").value;
    let email = document.getElementById("email").value;
    console.log(address);
    var inp = "paypal" //document.querySelector("#p_mod").value;
    if(inp == "paypal"){
        window.location.href = 'eth/' + (eth * 100) + '/' + address + '/' + key + '/' + email;
    }
}