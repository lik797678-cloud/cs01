import React from 'react';

const PortfolioView = () => {
    const [portfolio, setPortfolio] = React.useState([]);
    const [tradingHistory, setTradingHistory] = React.useState([]);

    React.useEffect(() => {
        fetchPortfolio();
        fetchTradingHistory();
    }, []);

    const fetchPortfolio = async () => {
        // Fetch user's beer portfolio data
        // Placeholder for actual API call
        const data = [
            { id: 1, name: 'IPA', quantity: 10 },
            { id: 2, name: 'Stout', quantity: 5 },
        ];
        setPortfolio(data);
    };

    const fetchTradingHistory = async () => {
        // Fetch user's trading history data
        // Placeholder for actual API call
        const history = [
            { date: '2026-02-01', beer: 'IPA', transaction: 'Bought', quantity: 5 },
            { date: '2026-02-05', beer: 'Stout', transaction: 'Sold', quantity: 2 },
        ];
        setTradingHistory(history);
    };

    return (
        <div>
            <h1>Your Beer Portfolio</h1>
            <ul>
                {portfolio.map(item => (
                    <li key={item.id}>{item.name}: {item.quantity}</li>
                ))}
            </ul>

            <h2>Trading History</h2>
            <ul>
                {tradingHistory.map((trade, index) => (
                    <li key={index}>{trade.date} - {trade.beer} - {trade.transaction}: {trade.quantity}</li>
                ))}
            </ul>
        </div>
    );
};

export default PortfolioView;