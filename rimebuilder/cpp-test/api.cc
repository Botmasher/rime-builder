//#include <boost/network/protocol/http/client.hpp> 		// cpp-netlib for url
#include <string>
#include <iostream>

int apiFrontConnectTest(int a) {
	int test = a + 2;
	return test;
}

// boost::network::http::client::response fetchRhymes() {
//   boost::network::http::client client;
//   boost::network::http::client::request request("https://api.datamuse.com/words?rel_rhy=forgetful");
//   request << boost::network::header("Connection", "close");
//   boost::network::http::client::response response = client.get(request);
//   std::cout << body(response);
//   return response;
// }
