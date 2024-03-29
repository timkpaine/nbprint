from IPython.display import HTML

from nbprint import Content


class ExampleFinanceTitleContent(Content):
    title: str = ""
    subtitle: str = ""
    date: str = ""
    css: str = """
div.row {
  padding-bottom: 10px;
}

h1 {
  font-family: sans-serif;
  font-size: 25px !important;
  padding-right: 15px;
  border-right: 2px solid black;
}

h2 {
  font-family: sans-serif;
  text-transform: uppercase;
  font-weight: bold !important;
  font-size: 12px !important;
  padding-left: 15px;
}

span {
  color: grey;
  font-size: 15px !important;
  font-style: italic;
}
    """

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
        <div class="row">
            <h1>{self.title}</h1>
            <h2>{self.subtitle}</h2>
        </div>
        <div class="row">
            <span>{self.date}</span>
        </div>
        """)


class ExampleFinanceStockHeadlineContent(Content):
    company_name: str = ""
    region: str = ""
    byline: str = ""
    color: str = ""
    css: str = """
div.row {
  padding-bottom: 10px;
}

h2:nth-child(1) {
  padding-right: 15px;
}

h2:nth-child(2) {
  padding-left: 15px;
}

h1 {
  font-weight: lighter;
}
"""

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
        <div class="row">
            <h2 style="color: {self.color}; border-right: 2px solid {self.color}">{self.company_name}</h2>
            <h2 style="color: {self.color};">{self.region}</h2>
        </div>
        <h1 class="nbprint-example-finance-heading-byline">{self.byline}</h1>
        """)


class ExampleFinanceReportAuthor(Content):
    name: str = ""
    title: str = ""
    email: str = ""
    phone: str = ""
    css: str = """

div.column > span:nth-child(1) {
  font-size: 12px;
  font-weight: bold;
}

div.column > span:nth-child(2) {
  font-size: 10px;
  text-transform: uppercase;
}

div.row {
  justify-content: space-between;
}

div.row > span:nth-child(1) {
  font-size: 10px;
}

div.row > span:nth-child(2) {
  font-family: monospace;
  font-size: 10px;
}

    """

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
            <div class="column">
                <span>{self.name}</span>
                <span>{self.title}</span>
                <div class="row">
                    <span>{self.email}</span>
                    <span>{self.phone}</span>
                </div>
            </div>
        """)


class ExampleFinanceStockQuickStats(Content):
    ticker: str = ""
    company_name: str = ""
    color: str = ""

    sector: str = ""
    country: str = ""
    region: str = ""

    rating: str
    view: str
    price_target: float

    share_price: float
    market_cap: str
    range_min: float
    range_max: float

    css: str = """
div.row {
  justify-content: space-between;
  font-size: 10px;
}

div.column > div.column > div.row:nth-child(1),
div.column > div.column > div.row:nth-child(2),
div.column > div.column > div.row:nth-child(3) {
  font-weight: bold;
}
"""

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
            <div class="column pt20">
                <div style="padding-left: 5px; background-color: {self.color}; color: white;">
                    <span>{self.company_name} ( {self.ticker} )</span>
                </div>
                <div class="row" style="font-size: 9px;">
                    <span>{self.sector}</span>
                    <span>/</span>
                    <span style="font-weight: bold;">{self.country}</span>
                </div>
                <div class="column">
                    <div class="row">
                        <span>Stock Rating</span>
                        <span>{self.rating}</span>
                    </div>
                    <div class="row">
                        <span>Industry View</span>
                        <span>{self.view}</span>
                    </div>
                    <div class="row">
                        <span>Price target</span>
                        <span>${self.price_target:.2f}</span>
                    </div>
                    <div class="row">
                        <span>Share Price</span>
                        <span>${self.share_price:.0f}</span>
                    </div>
                    <div class="row">
                        <span>Market Cap (mm)</span>
                        <span>${self.market_cap}</span>
                    </div>
                    <div class="row">
                        <span>52-Week Range</span>
                        <span>${self.range_min:.2f} - {self.range_max:.2f}</span>
                    </div>
                </div>
            </div>
        """)


class ExampleFinanceStockEarningsTable(Content):
    ticker: str = ""
    company_name: str = ""

    css: str = """
table {
  font-size: 10px !important;
}
table thead tr {
  font-weight: bold;
}
table tbody tr td:nth-child(1){
  font-weight: bold;
}
"""

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML("""
            <div class="pt10">
                <table>
                    <thead>
                        <tr>
                            <td>Fiscal Year Ending</td>
                            <td>3/24</td>
                            <td>3/25e</td>
                            <td>3/26e</td>
                            <td>3/27e</td>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>EPS ($)</td>
                            <td>(0.32)</td>
                            <td>(0.14)</td>
                            <td>0.11</td>
                            <td>0.31</td>
                        </tr>
                        <tr>
                            <td>Prior EPS ($)</td>
                            <td>(0.23)</td>
                            <td>(0.15)</td>
                            <td>0.03</td>
                            <td>0.13</td>
                        </tr>
                        <tr>
                            <td>P/E</td>
                            <td>NM</td>
                            <td>NM</td>
                            <td>NM</td>
                            <td>NM</td>
                        </tr>
                    </tbody>

                </table>
            </div>
        """)


class ExampleFinanceStockPTUpdate(Content):
    ticker: str = ""
    rating: str
    view: str
    price_target: float

    css: str = """
:scope div.row {
  margin-top: 15px;
  margin-bottom: 15px;
  justify-content: space-between;
}

div.row > div:nth-child(2),
div.row > div:nth-child(3) {
  padding-left: 20px;
  border-left: 1px solid black;
}

div.row > div > span:nth-child(1) {
  font-size: 10px;
}

div.row > div > span:nth-child(2) {
  font-size: 20px;
}

div.row div:nth-child(1) span:nth-child(1)::before {
  font-family: "Font Awesome 6 Free";
  font-weight: 900;
  content: '\\f201';
  display: none;
  width: 20px;
}

div.row div:nth-child(2) span:nth-child(1)::before {
  font-family: "Font Awesome 6 Free";
  content: '\\f06e';
  display: none;
}

div.row div:nth-child(3) span:nth-child(1)::before {
  font-family: "Font Awesome 6 Free";
  content: '\\f192';
  display: none;
}

svg {
  width: 15px;
  margin-right: 3px;
}
"""

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
        <div class="row">
            <div class="column">
                <span class="stock-rating">Stock Rating</span>
                <span>{self.rating}</span>
            </div>
            <div class="column">
                <span>Industry View</span>
                <span>{self.view}</span>
            </div>
            <div class="column">
                <span>Price Target</span>
                <span>${self.price_target:.2f}</span>
            </div>
        </div>
        """)


class ExampleFinanceStockHeadline(Content):
    text: str = ""

    css: str = """
:scope span {
  font-size: 20px;
}
"""

    def __call__(self, ctx=None, *args, **kwargs):
        return HTML(f"""
            <span>{self.text}</span>
        """)
